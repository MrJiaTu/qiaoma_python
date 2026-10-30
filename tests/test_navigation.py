"""F4 二级视图：选中课题后先看到该课题的题目列表。

不启用快速防抖 fixture：variables01 是一道能通过的题，防抖压到毫秒后
「加载题目 -> 自动检查 -> 自动进下一题」会在测试的 pause 里跑完。
"""
from __future__ import annotations

from pathlib import Path

from textual.widgets import Label, ListView

from qiaoma.app import QiaomaApp
from qiaoma.core.manifest import load_manifest
from qiaoma.core.state import State
from qiaoma.screens.exlist import ExerciseListModal, format_exercise_line
from qiaoma.screens.exercise import ExerciseScreen
from qiaoma.screens.picker import TopicPickerScreen

# 来自 tests/conftest.py 的 MINI_INFO_TOML：variables 课题的描述
VARIABLES_DESCRIPTION = "从饭卡找零开始认识变量"


def test_format_exercise_line_three_states(workspace: Path):
    """共享行渲染：已完成 ✔、当前 ▶、其余 · 都带题号与标题。"""
    manifest = load_manifest(workspace)
    state = State.load(workspace)
    variables01 = manifest.exercise("variables01")

    state.set_current("variables01")
    line = format_exercise_line(state, manifest, variables01)
    assert "▶" in line and "variables01" in line and "饭卡找零" in line

    state.mark_done("variables01")
    line = format_exercise_line(state, manifest, variables01)
    assert "✔" in line and "饭卡找零" in line

    strings01 = manifest.exercise("strings01")
    line = format_exercise_line(state, manifest, strings01)
    assert "·" in line and "打招呼" in line


async def test_f4_topic_selection_opens_exercise_sublist(workspace: Path):
    """回车不再直接跳题，而是先弹本课题的题目列表。"""
    app = QiaomaApp(workspace)
    async with app.run_test(size=(100, 32)) as pilot:
        await pilot.pause()
        await pilot.press("f4")
        await pilot.pause()
        await pilot.press("enter")  # 高亮的第一门是 variables
        await pilot.pause()
        assert isinstance(app.screen, ExerciseListModal)
        assert app.screen.topic_id == "variables"


async def test_sublist_header_shows_topic_description(workspace: Path):
    """课题描述终于有地方显示了。"""
    app = QiaomaApp(workspace)
    async with app.run_test(size=(100, 32)) as pilot:
        await pilot.pause()
        await pilot.press("f4")
        await pilot.pause()
        await pilot.press("enter")
        await pilot.pause()
        labels = " ".join(str(label.render()) for label in app.screen.query(Label))
        assert VARIABLES_DESCRIPTION in labels
        assert "变量与类型" in labels


async def test_sublist_esc_returns_to_topic_picker(workspace: Path):
    """子列表 Esc 回课题列表，不是做题界面。"""
    app = QiaomaApp(workspace)
    async with app.run_test(size=(100, 32)) as pilot:
        await pilot.pause()
        await pilot.press("f4")
        await pilot.pause()
        await pilot.press("enter")
        await pilot.pause()
        await pilot.press("escape")
        await pilot.pause()
        assert isinstance(app.screen, TopicPickerScreen)


async def test_sublist_enter_loads_exercise(workspace: Path):
    """子列表回车：两层弹窗都关掉，开在选定的题上。"""
    app = QiaomaApp(workspace)
    async with app.run_test(size=(100, 32)) as pilot:
        await pilot.pause()
        await pilot.press("f4")
        await pilot.pause()
        await pilot.press("enter")
        await pilot.pause()
        await pilot.press("enter")  # variables01（未完成的第一题）
        await pilot.pause()
        assert isinstance(app.screen, ExerciseScreen)
        assert app.screen.exercise_id == "variables01"
        assert app.state.current_id == "variables01"


async def test_sublist_cursor_starts_on_first_pending(workspace: Path):
    """保留旧快速路径：光标落在该课题第一道未完成的题上。"""
    state = State.load(workspace)
    state.mark_done("variables01")
    state.save()

    app = QiaomaApp(workspace)
    async with app.run_test(size=(100, 32)) as pilot:
        await pilot.pause()
        await pilot.press("f4")
        await pilot.pause()
        await pilot.press("enter")
        await pilot.pause()
        assert app.screen.query_one(ListView).index == 1  # variables02


async def test_f4_sublist_also_hides_locked_title(workspace: Path):
    """课题子列表与 F3 共用行渲染，锁定题同样隐藏标题。"""
    app = QiaomaApp(workspace)
    async with app.run_test(size=(100, 32)) as pilot:
        await pilot.pause()
        await pilot.press("f4")
        await pilot.pause()
        await pilot.press("enter")  # 进 variables 的子列表
        await pilot.pause()
        labels = " ".join(str(label.render()) for label in app.screen.query(Label))
        assert "🔒" in labels
        assert "年龄计算" not in labels  # variables02 被锁
        assert "饭卡找零" in labels  # variables01 未锁，标题照常可见
