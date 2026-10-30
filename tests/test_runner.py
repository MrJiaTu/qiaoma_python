"""runner 模块测试：子进程判题。"""
from __future__ import annotations

from pathlib import Path

from qiaoma.core.manifest import load_manifest
from qiaoma.core.runner import run_check


def test_passing_exercise(workspace: Path):
    manifest = load_manifest(workspace)
    result = run_check(workspace, manifest.exercise("variables01"))
    assert result.status == "passed"


def test_blocked_by_not_done_marker(workspace: Path):
    manifest = load_manifest(workspace)
    result = run_check(workspace, manifest.exercise("variables02"))
    assert result.status == "blocked"
    assert "我还没做完" in result.message


def test_failing_check_reports_message(workspace: Path):
    manifest = load_manifest(workspace)
    result = run_check(workspace, manifest.exercise("strings01"))
    assert result.status == "failed"
    assert "故意失败的检查" in result.message


def test_runtime_error_is_failed(workspace: Path):
    manifest = load_manifest(workspace)
    ex = manifest.exercise("variables01")
    ex.path(workspace).write_text("x = 1 / 0\n", encoding="utf-8")
    result = run_check(workspace, ex)
    assert result.status == "failed"
    assert "ZeroDivisionError" in result.message


def test_hangs_are_timed_out(workspace: Path):
    manifest = load_manifest(workspace)
    ex = manifest.exercise("variables01")
    ex.path(workspace).write_text("while True:\n    pass\n", encoding="utf-8")
    result = run_check(workspace, ex, timeout=2)
    assert result.status == "failed"
    assert "超时" in result.message
