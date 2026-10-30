"""题目列表弹窗：F3 的全局列表，或 F4 选定课题后的子列表。"""
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Label, ListItem, ListView

if TYPE_CHECKING:  # pragma: no cover
    from ..app import QiaomaApp
    from ..core.manifest import Exercise, Manifest
    from ..core.state import State


class ExerciseItem(ListItem):
    def __init__(self, exercise_id: str, label: str) -> None:
        super().__init__(Label(label))
        self.exercise_id = exercise_id


def format_exercise_line(state: State, manifest: Manifest, exercise: Exercise) -> str:
    """返回一行列表文本（含 Rich 标记）。

    F3 全局列表与课题子列表共用，避免两处文案漂移。
    """
    if state.is_done(exercise.id):
        mark, title = "[green]✔[/green]", exercise.title
    elif state.lock_message(manifest, exercise) is not None:
        mark, title = "[dim]🔒[/dim]", "???"
    elif exercise.id == state.current_id:
        mark, title = "[yellow]▶[/yellow]", exercise.title
    else:
        mark, title = "[dim]·[/dim]", exercise.title
    return f"{mark} {exercise.id} {title}"


class ExerciseListModal(ModalScreen[Optional[str]]):
    """选择后返回 exercise_id；按 Esc 返回 None。

    ``topic_id`` 不为 None 时只列出该课题的题目，并在列表上方给出课题名与描述。
    锁定题仍占一行，但标题隐成 ???，选中它不会关闭弹窗。
    """

    DEFAULT_CSS = """
    ExerciseListModal {
        align: center middle;
    }
    ExerciseListModal > Label {
        width: 80;
        height: auto;
    }
    ExerciseListModal > ListView {
        width: 80;
        height: 85%;
        border: round $accent;
        background: $surface;
        padding: 1 2;
    }
    """

    BINDINGS = [("escape", "cancel", "返回")]

    def __init__(self, app_ref: "QiaomaApp", topic_id: Optional[str] = None) -> None:
        super().__init__()
        self._app_ref = app_ref
        self.topic_id = topic_id

    def compose(self) -> ComposeResult:
        app = self._app_ref
        if self.topic_id is None:
            exercises = app.manifest.exercises
        else:
            topic = next(t for t in app.manifest.topics if t.id == self.topic_id)
            done, total = app.state.topic_progress(app.manifest, topic.id)
            yield Label(
                f"[bold]{topic.track} · {topic.name}[/bold]  ({done}/{total})\n"
                f"[dim]{topic.description}[/dim]"
            )
            exercises = app.manifest.exercises_for(self.topic_id)
        items = [
            ExerciseItem(ex.id, format_exercise_line(app.state, app.manifest, ex))
            for ex in exercises
        ]
        yield ListView(*items)

    def on_mount(self) -> None:
        list_view = self.query_one(ListView)
        if self.topic_id is not None:
            # 光标停在该课题第一道未完成的题上，直接回车即进入该题
            siblings = self._app_ref.manifest.exercises_for(self.topic_id)
            first_pending = next(
                (
                    i
                    for i, ex in enumerate(siblings)
                    if not self._app_ref.state.is_done(ex.id)
                ),
                0,
            )
            if siblings:
                list_view.index = first_pending
        list_view.focus()

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        if not isinstance(event.item, ExerciseItem):
            return
        app = self._app_ref
        exercise = app.manifest.exercise(event.item.exercise_id)
        message = app.state.lock_message(app.manifest, exercise)
        if message is not None:
            # 弹窗不关闭，学员才能看到提示
            self.notify(message, severity="error")
            return
        self.dismiss(event.item.exercise_id)

    def action_cancel(self) -> None:
        self.dismiss(None)
