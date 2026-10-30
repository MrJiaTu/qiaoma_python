"""CLI 层的顺序解锁拦截：不留 hint/run/reset 后门。"""
from __future__ import annotations

from pathlib import Path

import pytest

from qiaoma.cli import main
from qiaoma.core.manifest import load_manifest
from qiaoma.core.state import State

# conftest 迷你工作区里 variables02 的提示文本，用于断言未泄露
VARIABLES02_HINT = "用当前年份减去出生年份"


def argv(*parts: str) -> list:
    return list(parts)


def test_hint_refuses_locked_exercise(workspace: Path, capsys):
    with pytest.raises(SystemExit) as exc:
        main(argv("-w", str(workspace), "hint", "variables02"))
    assert exc.value.code == 1
    out = capsys.readouterr().out
    assert "未解锁" in out
    assert VARIABLES02_HINT not in out


def test_run_refuses_locked_exercise(workspace: Path, capsys):
    with pytest.raises(SystemExit) as exc:
        main(argv("-w", str(workspace), "run", "variables02"))
    assert exc.value.code == 1
    out = capsys.readouterr().out
    assert "未解锁" in out
    # 判题根本没跑：被拦时不会输出题目代码的任何运行信息
    assert "我还没做完" not in out


def test_reset_refuses_locked_exercise(workspace: Path, capsys):
    manifest = load_manifest(workspace)
    exercise = manifest.exercise("variables02")
    edited = "# 我改了一半\n"
    exercise.path(workspace).write_text(edited, encoding="utf-8")

    with pytest.raises(SystemExit) as exc:
        main(argv("-w", str(workspace), "reset", "variables02", "--yes"))
    assert exc.value.code == 1
    assert exercise.path(workspace).read_text(encoding="utf-8") == edited
    assert "未解锁" in capsys.readouterr().out


def test_hint_allows_first_exercise_of_topic(workspace: Path, capsys):
    main(argv("-w", str(workspace), "hint", "variables01"))  # 不应抛 SystemExit
    out = capsys.readouterr().out
    assert "先算出总价" in out


def test_hint_allows_after_predecessor_done(workspace: Path, capsys):
    state = State.load(workspace)
    state.mark_done("variables01")
    state.save()

    main(argv("-w", str(workspace), "hint", "variables02"))
    assert VARIABLES02_HINT in capsys.readouterr().out
