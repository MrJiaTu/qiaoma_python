"""TUI 冒烟测试：用 Textual Pilot 驱动真实界面。"""
from __future__ import annotations

from pathlib import Path

import pytest
from textual.widgets import Label

import qiaoma.screens.exercise as exercise_module
from qiaoma.app import QiaomaApp
from qiaoma.core.state import State
from qiaoma.screens.exercise import ExerciseScreen


@pytest.fixture
def fast_ui(monkeypatch: pytest.MonkeyPatch):
    """把防抖与跳转延迟调到最小，测试不用等。"""
    monkeypatch.setattr(exercise_module, "CHECK_DEBOUNCE_SECONDS", 0.05)
    monkeypatch.setattr(exercise_module, "ADVANCE_DELAY_SECONDS", 0.1)


async def test_opens_first_pending_exercise(workspace: Path, fast_ui):
    app = QiaomaApp(workspace)
    async with app.run_test(size=(100, 32)) as pilot:
        await pilot.pause()
        screen = app.screen
        assert isinstance(screen, ExerciseScreen)
        assert screen.exercise_id == "variables01"
        title = str(screen.query_one("#title-bar").content)
        assert "饭卡找零" in title


async def test_save_and_check_advances_on_pass(workspace: Path, fast_ui, monkeypatch):
    # 关掉防抖自动检查，确保这条用例真的在验 Ctrl+S 这条路
    monkeypatch.setattr(exercise_module, "CHECK_DEBOUNCE_SECONDS", 600)
    app = QiaomaApp(workspace)
    async with app.run_test(size=(100, 32)) as pilot:
        await pilot.pause()
        await pilot.press("ctrl+s")
        await pilot.pause(0.5)
        state = State.load(workspace)
        assert state.is_done("variables01")
        await pilot.pause(1.0)  # 等待自动进入下一题
        assert app.screen.exercise_id == "variables02"  # type: ignore[union-attr]


async def test_blocked_exercise_shows_marker_message(workspace: Path, fast_ui):
    app = QiaomaApp(workspace)
    async with app.run_test(size=(100, 32)) as pilot:
        await pilot.pause()
        screen = app.screen
        assert isinstance(screen, ExerciseScreen)
        app.state.mark_done("variables01")  # 解锁 variables02 才能打开它
        screen.load_exercise("variables02")
        await pilot.pause()
        await pilot.press("ctrl+s")
        await pilot.pause(0.5)
        assert "我还没做完" in str(screen.result_panel.content)


async def test_f4_opens_topic_picker_and_esc_cancels(workspace: Path, fast_ui):
    app = QiaomaApp(workspace)
    async with app.run_test(size=(100, 32)) as pilot:
        await pilot.pause()
        await pilot.press("f4")
        await pilot.pause()
        from qiaoma.screens.picker import TopicPickerScreen

        assert isinstance(app.screen, TopicPickerScreen)
        await pilot.press("escape")
        await pilot.pause()
        assert isinstance(app.screen, ExerciseScreen)


async def test_f1_toggles_hint_panel(workspace: Path, fast_ui):
    app = QiaomaApp(workspace)
    async with app.run_test(size=(100, 32)) as pilot:
        await pilot.pause()
        screen = app.screen
        assert isinstance(screen, ExerciseScreen)
        assert not screen.hint_panel.display
        await pilot.press("f1")
        await pilot.pause()
        assert screen.hint_panel.display


# 下面两条不按 ctrl+s：把防抖调到 600 秒，避免自动检查把界面带离断言目标。
async def test_locked_exercise_cannot_be_opened(workspace: Path, monkeypatch):
    """未解锁的题打不开：不切换题目，也不改写 current_id。"""
    monkeypatch.setattr(exercise_module, "CHECK_DEBOUNCE_SECONDS", 600)
    app = QiaomaApp(workspace)
    async with app.run_test(size=(100, 32)) as pilot:
        await pilot.pause()
        screen = app.screen
        assert isinstance(screen, ExerciseScreen)
        screen.load_exercise("variables02")
        await pilot.pause()
        assert screen.exercise_id == "variables01"
        assert app.state.current_id == "variables01"


async def test_start_falls_back_when_current_is_locked(workspace: Path, monkeypatch):
    """损坏的 state.json 把 current 指向锁定题时，回退到 first_pending。"""
    monkeypatch.setattr(exercise_module, "CHECK_DEBOUNCE_SECONDS", 600)
    state = State.load(workspace)
    state.set_current("variables02")
    state.save()

    app = QiaomaApp(workspace)
    async with app.run_test(size=(100, 32)) as pilot:
        await pilot.pause()
        screen = app.screen
        assert isinstance(screen, ExerciseScreen)
        assert screen.exercise_id == "variables01"
        # 编辑器必须有内容：这是为了防「拒绝切换后留下空白屏幕」。
        # 内容取 conftest 的 PASSING_EXERCISE，不是真实课程里的饭卡代码。
        assert screen.editor.text.strip()
        assert "change = 100 - 35" in screen.editor.text


def make_two_topic_workspace(root: Path) -> Path:
    """两门课题：A 只有一题且保持未完成，B 有两题。"""
    ws = root / "advance"
    for topic in ("a", "b"):
        (ws / "exercises" / topic).mkdir(parents=True)
        (ws / "checks" / topic).mkdir(parents=True)
    (ws / "info.toml").write_text(
        "[[topics]]\nid = \"a\"\nname = \"课题 A\"\ntrack = \"初级\"\n\n"
        "[[topics]]\nid = \"b\"\nname = \"课题 B\"\ntrack = \"初级\"\n\n"
        "[[exercises]]\nid = \"a01\"\ntopic = \"a\"\ntitle = \"A 的第一题\"\n\n"
        "[[exercises]]\nid = \"b01\"\ntopic = \"b\"\ntitle = \"B 的第一题\"\n\n"
        "[[exercises]]\nid = \"b02\"\ntopic = \"b\"\ntitle = \"B 的第二题\"\n",
        encoding="utf-8",
    )
    for exercise_id, topic in (("a01", "a"), ("b01", "b"), ("b02", "b")):
        (ws / "exercises" / topic / f"{exercise_id}.py").write_text(
            "value = 1\n", encoding="utf-8"
        )
        (ws / "checks" / topic / f"{exercise_id}.py").write_text(
            "assert value == 1\n", encoding="utf-8"
        )
    return ws


async def test_pass_keeps_progress_inside_topic(tmp_path: Path, monkeypatch):
    """在第二门课题里通过一题，应进入本课题下一题，而不是全局第一道未完成。"""
    monkeypatch.setattr(exercise_module, "CHECK_DEBOUNCE_SECONDS", 600)
    monkeypatch.setattr(exercise_module, "ADVANCE_DELAY_SECONDS", 0.1)
    ws = make_two_topic_workspace(tmp_path)

    app = QiaomaApp(ws)
    async with app.run_test(size=(100, 32)) as pilot:
        await pilot.pause()
        screen = app.screen
        assert isinstance(screen, ExerciseScreen)
        assert screen.exercise_id == "a01"  # 全局第一道未完成
        screen.load_exercise("b01")  # 课题 B 的首题，可以访问
        await pilot.pause()
        await pilot.press("ctrl+s")
        for _ in range(30):
            await pilot.pause(0.1)
            if app.screen.exercise_id == "b02":
                break
        assert app.screen.exercise_id == "b02"


async def test_f3_locked_exercise_hides_title(workspace: Path):
    """锁定题显示 ??? —— 标题本身就是剧透。"""
    app = QiaomaApp(workspace)
    async with app.run_test(size=(100, 32)) as pilot:
        await pilot.pause()
        await pilot.press("f3")
        await pilot.pause()
        labels = " ".join(str(label.render()) for label in app.screen.query(Label))
        assert "variables01" in labels
        assert "variables02" in labels
        assert "🔒" in labels
        assert "年龄计算" not in labels  # variables02 的标题不得出现


async def test_f3_locked_selection_keeps_modal_open(workspace: Path):
    """选中锁定题：不跳转、不关弹窗，只给一句解释。"""
    app = QiaomaApp(workspace)
    async with app.run_test(size=(100, 32)) as pilot:
        await pilot.pause()
        exercise_screen = app.screen
        await pilot.press("f3")
        await pilot.pause()
        await pilot.press("down")  # 光标从 variables01 移到 variables02
        await pilot.press("enter")
        await pilot.pause()
        from qiaoma.screens.exlist import ExerciseListModal

        assert isinstance(app.screen, ExerciseListModal)
        assert exercise_screen.exercise_id == "variables01"
