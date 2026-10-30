"""做题主界面：编辑器 + 判题结果 + 提示面板。"""
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from textual import work
from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.timer import Timer
from textual.widgets import Footer, Static, TextArea
from rich.text import Text

from ..core.reset import reset_exercise
from ..core.runner import run_check

if TYPE_CHECKING:  # pragma: no cover
    from ..app import QiaomaApp

CHECK_DEBOUNCE_SECONDS = 2.0
ADVANCE_DELAY_SECONDS = 1.2


class TitleBar(Static):
    """顶部标题栏：课题、题目标题与总进度。"""


class ResultPanel(Static):
    """判题结果面板。"""

    DEFAULT_CSS = """
    ResultPanel {
        height: auto;
        min-height: 3;
        padding: 1 2;
        border: round $primary;
    }
    ResultPanel.passed { border: round $success; }
    ResultPanel.failed { border: round $error; }
    ResultPanel.blocked { border: round $warning; }
    """

    def show_result(self, status: str, message: str) -> None:
        self.remove_class("passed", "failed", "blocked")
        self.add_class(status)
        # 判题消息含学员代码输出，按纯文本渲染，避免被当作 Rich 标记解析
        self.update(Text(message))


class HintPanel(Static):
    """提示面板，F1 开关。"""

    DEFAULT_CSS = """
    HintPanel {
        height: auto;
        padding: 1 2;
        border: round $accent;
        display: none;
    }
    """


class ExerciseScreen(Screen):
    """单题界面：修复代码 → 自动判题 → 通过进入下一题。"""

    BINDINGS = [
        ("f1", "toggle_hint", "提示 F1"),
        ("f2", "reset", "重置 F2"),
        ("f3", "exercise_list", "题目 F3"),
        ("f4", "topic_picker", "课题 F4"),
        ("ctrl+s", "save_and_check", "检查 Ctrl+S"),
        ("ctrl+q", "quit", "退出"),
        ("escape", "quit", "退出"),
    ]

    def __init__(
        self,
        app_ref: "QiaomaApp",
        exercise_id: str,
        open_picker: bool = False,
    ) -> None:
        super().__init__()
        self._app_ref = app_ref
        self.exercise_id = exercise_id
        self._open_picker = open_picker
        self._debounce_timer: Optional[Timer] = None
        self._advance_timer: Optional[Timer] = None

    # ---- 布局 ----

    def compose(self) -> ComposeResult:
        yield TitleBar(id="title-bar")
        yield TextArea(language="python", id="editor")
        with Vertical(id="panels"):
            yield ResultPanel(id="result")
            yield HintPanel(id="hints")
        yield Footer()

    def on_mount(self) -> None:
        self.editor.focus()
        self.load_exercise(self.exercise_id)
        if self._open_picker:
            self._open_picker = False
            self.call_after_refresh(self.action_topic_picker)

    # ---- 属性快捷方式 ----

    @property
    def editor(self) -> TextArea:
        return self.query_one("#editor", TextArea)

    @property
    def result_panel(self) -> ResultPanel:
        return self.query_one("#result", ResultPanel)

    @property
    def hint_panel(self) -> HintPanel:
        return self.query_one("#hints", HintPanel)

    # ---- 题目加载 ----

    def load_exercise(self, exercise_id: str) -> None:
        app = self._app_ref
        exercise = app.manifest.exercise(exercise_id)
        # 先停掉待执行的计时器：即使这次切换被拒绝，也不该让上一题
        # 遗留的自动跳转在一秒后把界面带走。
        if self._advance_timer is not None:
            self._advance_timer.stop()
            self._advance_timer = None
        if self._debounce_timer is not None:
            self._debounce_timer.stop()
            self._debounce_timer = None
        message = app.state.lock_message(app.manifest, exercise)
        if message is not None:
            # 锁定题：不切题、不写 current_id、不碰编辑器
            self.notify(message, severity="error")
            return
        self.exercise_id = exercise_id
        app.state.set_current(exercise_id)
        app.state.save()

        source = exercise.path(app.workspace).read_text(encoding="utf-8")
        self.editor.load_text(source)
        self.editor.focus()

        topic = next(t for t in app.manifest.topics if t.id == exercise.topic)
        done, total = app.state.topic_progress(app.manifest, topic.id)
        all_done = sum(1 for e in app.manifest.exercises if app.state.is_done(e.id))
        self.query_one("#title-bar", TitleBar).update(
            f"[bold]{topic.track} · {topic.name}[/bold]  "
            f"[b]{exercise.id} {exercise.title}[/b]  "
            f"课题 {done}/{total} · 总进度 {all_done}/{len(app.manifest.exercises)}"
        )
        self.result_panel.show_result(
            "blocked", "修复代码、删除未完成标记行，检查会自动重跑（Ctrl+S 立即检查）。"
        )
        self._update_hints()

    def _update_hints(self) -> None:
        exercise = self._app_ref.manifest.exercise(self.exercise_id)
        if exercise.hints:
            lines = "\n".join(
                f"[dim]提示 {i}:[/dim] {hint}" for i, hint in enumerate(exercise.hints, 1)
            )
        else:
            lines = "这道题没有提示，直接看报错信息找线索吧。"
        self.hint_panel.update(lines)

    # ---- 判题 ----

    def on_text_area_changed(self, event: TextArea.Changed) -> None:
        """编辑停顿后自动保存并判题。"""
        if self._debounce_timer is not None:
            self._debounce_timer.stop()
        self._debounce_timer = self.set_timer(CHECK_DEBOUNCE_SECONDS, self._auto_check)

    def _auto_check(self) -> None:
        self.save_current_file()
        self._launch_check()

    def action_save_and_check(self) -> None:
        self.save_current_file()
        self._launch_check()

    def save_current_file(self) -> None:
        app = self._app_ref
        exercise = app.manifest.exercise(self.exercise_id)
        exercise.path(app.workspace).write_text(self.editor.text, encoding="utf-8")

    def _launch_check(self) -> None:
        self.result_panel.show_result("blocked", "正在检查……")
        self._run_check_worker(self.exercise_id)

    @work(thread=True, exclusive=True, group="check")
    def _run_check_worker(self, exercise_id: str) -> None:
        app = self._app_ref
        result = run_check(app.workspace, app.manifest.exercise(exercise_id))
        self.app.call_from_thread(self._apply_result, exercise_id, result)

    def _apply_result(self, exercise_id: str, result) -> None:
        if exercise_id != self.exercise_id:
            return  # 已切换到别的题，丢弃过期结果
        app = self._app_ref
        if result.status == "passed":
            app.state.mark_done(exercise_id)
            app.state.save()
            self.result_panel.show_result("passed", f"✔ {result.message}")
            # 优先按课程顺序进下一题（同一课题内即本课题下一题）；
            # 若它仍被锁（进度数据有空洞），回退到队列首道可访问题。
            next_ex = app.state.next_after(exercise_id, app.manifest)
            if next_ex is None or not app.state.is_unlocked(app.manifest, next_ex):
                next_ex = app.state.first_pending(app.manifest)
            if next_ex is None:
                self.notify("全部 280 道题已完成，恭喜毕业！", severity="information")
            else:
                self.notify(f"通过！{ADVANCE_DELAY_SECONDS:.0f} 秒后进入下一题……")
                self._advance_timer = self.set_timer(
                    ADVANCE_DELAY_SECONDS, lambda: self.load_exercise(next_ex.id)
                )
        else:
            self.result_panel.show_result(result.status, result.message)

    # ---- 快捷键动作 ----

    def action_toggle_hint(self) -> None:
        panel = self.hint_panel
        panel.display = not panel.display

    def action_reset(self) -> None:
        app = self._app_ref
        exercise = app.manifest.exercise(self.exercise_id)
        reset_exercise(app.workspace, exercise)
        self.load_exercise(self.exercise_id)
        self.notify("已重置为原始题目。")

    def action_exercise_list(self) -> None:
        from .exlist import ExerciseListModal

        def on_picked(exercise_id: Optional[str]) -> None:
            if exercise_id:
                self.load_exercise(exercise_id)

        self.app.push_screen(ExerciseListModal(self._app_ref), on_picked)

    def action_topic_picker(self) -> None:
        from .picker import TopicPickerScreen

        def on_picked(exercise_id: Optional[str]) -> None:
            if exercise_id:
                self.load_exercise(exercise_id)

        self.app.push_screen(TopicPickerScreen(self._app_ref), on_picked)
