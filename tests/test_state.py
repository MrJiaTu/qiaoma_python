"""state 模块测试：进度持久化与题目导航。"""
from __future__ import annotations

from pathlib import Path

from qiaoma.core.manifest import load_manifest
from qiaoma.core.state import State


def test_fresh_state_has_nothing_done(workspace: Path):
    state = State.load(workspace)
    assert state.completed == set()
    assert state.current_id is None


def test_mark_done_and_persist(workspace: Path):
    state = State.load(workspace)
    state.mark_done("variables01")
    state.save()

    reloaded = State.load(workspace)
    assert reloaded.is_done("variables01")
    assert not reloaded.is_done("variables02")


def test_current_exercise_roundtrip(workspace: Path):
    state = State.load(workspace)
    state.set_current("variables02")
    state.save()
    assert State.load(workspace).current_id == "variables02"


def test_first_pending_skips_done(workspace: Path):
    manifest = load_manifest(workspace)
    state = State.load(workspace)
    assert state.first_pending(manifest).id == "variables01"

    state.mark_done("variables01")
    assert state.first_pending(manifest).id == "variables02"

    state.mark_done("variables02")
    state.mark_done("strings01")
    assert state.first_pending(manifest) is None


def test_next_after(workspace: Path):
    manifest = load_manifest(workspace)
    state = State.load(workspace)
    assert state.next_after("variables01", manifest).id == "variables02"
    assert state.next_after("variables02", manifest).id == "strings01"
    assert state.next_after("strings01", manifest) is None


def test_topic_progress(workspace: Path):
    manifest = load_manifest(workspace)
    state = State.load(workspace)
    assert state.topic_progress(manifest, "variables") == (0, 2)
    state.mark_done("variables01")
    assert state.topic_progress(manifest, "variables") == (1, 2)
    assert state.topic_progress(manifest, "strings") == (0, 1)
