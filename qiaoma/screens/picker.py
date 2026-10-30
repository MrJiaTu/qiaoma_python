"""课题选择器：选中课题后先看该课题的题目列表。"""
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Label, ListItem, ListView

from .exlist import ExerciseListModal

if TYPE_CHECKING:  # pragma: no cover
    from ..app import QiaomaApp


class TopicItem(ListItem):
    def __init__(self, topic_id: str, label: str) -> None:
        super().__init__(Label(label))
        self.topic_id = topic_id


class TopicPickerScreen(ModalScreen[Optional[str]]):
    """课题选择器。

    注意 dismiss 结果的语义：返回的是 **exercise_id**，不是 topic_id。
    选中课题后先 push 该课题的题目子列表，子列表选定才 dismiss。
    """

    DEFAULT_CSS = """
    TopicPickerScreen {
        align: center middle;
    }
    TopicPickerScreen > ListView {
        width: 76;
        height: 80%;
        border: round $accent;
        background: $surface;
        padding: 1 2;
    }
    """

    BINDINGS = [("escape", "cancel", "返回")]

    def __init__(self, app_ref: "QiaomaApp") -> None:
        super().__init__()
        self._app_ref = app_ref

    def compose(self) -> ComposeResult:
        app = self._app_ref
        items = []
        for topic in app.manifest.topics:
            done, total = app.state.topic_progress(app.manifest, topic.id)
            mark = "✔" if done == total and total else " "
            items.append(
                TopicItem(
                    topic.id,
                    f"{mark} [{topic.track}] {topic.name}  ({done}/{total})",
                )
            )
        yield ListView(*items)

    def on_mount(self) -> None:
        self.query_one(ListView).focus()

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        if not isinstance(event.item, TopicItem):
            return
        self.app.push_screen(
            ExerciseListModal(self._app_ref, topic_id=event.item.topic_id),
            self._on_exercise_chosen,
        )

    def _on_exercise_chosen(self, exercise_id: Optional[str]) -> None:
        if exercise_id is not None:
            self.dismiss(exercise_id)
        # None = 子列表按了 Esc，留在课题列表让用户换一门

    def action_cancel(self) -> None:
        self.dismiss(None)
