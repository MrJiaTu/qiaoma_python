"""代码评审回归测试：topics 启动、init 不覆盖、runner 兜底。"""
from __future__ import annotations

from pathlib import Path

import pytest

import qiaoma.screens.exercise as exercise_module
from qiaoma.app import QiaomaApp
from qiaoma.core.manifest import load_manifest
from qiaoma.core.runner import run_check
from qiaoma.core.workspace import init_workspace
from qiaoma.screens.picker import TopicPickerScreen


@pytest.fixture
def fast_ui(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(exercise_module, "CHECK_DEBOUNCE_SECONDS", 0.05)
    monkeypatch.setattr(exercise_module, "ADVANCE_DELAY_SECONDS", 0.1)


async def test_topics_command_opens_picker(workspace: Path, fast_ui):
    app = QiaomaApp(workspace, start_with_picker=True)
    async with app.run_test(size=(100, 32)) as pilot:
        await pilot.pause()
        await pilot.pause()
        assert isinstance(app.screen, TopicPickerScreen)


def test_reinit_preserves_learner_edits(tmp_path: Path):
    target = tmp_path / "learn"
    init_workspace(target)
    manifest = load_manifest(target)
    first = manifest.exercises[0]
    first.path(target).write_text("# 我改了一半\n", encoding="utf-8")

    init_workspace(target)
    assert first.path(target).read_text(encoding="utf-8") == "# 我改了一半\n"


def test_run_check_never_raises_on_missing_file(workspace: Path):
    manifest = load_manifest(workspace)
    exercise = manifest.exercise("variables01")
    exercise.path(workspace).unlink()
    result = run_check(workspace, exercise)
    assert result.status == "failed"
    assert "判题出错" in result.message
