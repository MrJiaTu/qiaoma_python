"""敲码 TUI 应用入口。"""
from __future__ import annotations

from pathlib import Path

from textual.app import App

from .core.manifest import load_manifest
from .core.state import State
from .screens.exercise import ExerciseScreen


class QiaomaApp(App):
    """终端手敲 Python 学习应用。"""

    TITLE = "敲码 qiaoma"
    SUB_TITLE = "在终端里手敲 Python"

    CSS = """
    Screen {
        layout: vertical;
    }
    #title-bar {
        dock: top;
        height: 1;
        background: $primary;
        color: $text;
        padding: 0 1;
    }
    #editor {
        height: 1fr;
    }
    #panels {
        height: auto;
        max-height: 45%;
    }
    """

    def __init__(self, workspace: Path, start_with_picker: bool = False) -> None:
        super().__init__()
        self.workspace = Path(workspace)
        self.manifest = load_manifest(self.workspace)
        self.state = State.load(self.workspace)
        self._start_with_picker = start_with_picker

    def on_mount(self) -> None:
        current = None
        if self.state.current_id and not self.state.is_done(self.state.current_id):
            try:
                exercise = self.manifest.exercise(self.state.current_id)
            except KeyError:
                exercise = None
            # 锁定题不能直接打开：守卫会让屏幕停在未加载过文件的空界面
            if exercise is not None and self.state.is_unlocked(
                self.manifest, exercise
            ):
                current = exercise
        start = current or self.state.first_pending(self.manifest)
        if start is None:
            self.exit(message="所有题目都已完成，恭喜毕业！")
            return
        screen = ExerciseScreen(self, start.id, open_picker=self._start_with_picker)
        self.push_screen(screen)
