"""顺序解锁判定：core 层纯函数测试，不涉及界面。"""
from __future__ import annotations

from pathlib import Path
from typing import Iterable

from qiaoma.core.manifest import Exercise, Manifest, Topic, load_manifest
from qiaoma.core.state import State


def three_exercise_manifest() -> Manifest:
    """内存里造一门三题的课题，用来构造 completed 空洞。

    迷你工作区（tests/conftest.py）每门课题最多 2 题，不足以
    区分「物理前一个」和「第一个未完成的前驱」。
    """
    topic = Topic(id="t", name="测试课题", track="初级")
    exercises = [
        Exercise(id=f"t{i:02d}", topic="t", title=f"题{i:02d}") for i in (1, 2, 3)
    ]
    return Manifest(topics=[topic], exercises=exercises)


def in_memory_state(completed: Iterable[str]) -> State:
    """不落盘的 State，只做判定。"""
    return State(Path("unused"), completed=set(completed), current_id=None)


def test_first_exercise_of_each_topic_always_unlocked(workspace: Path):
    manifest = load_manifest(workspace)
    state = State.load(workspace)
    assert state.is_unlocked(manifest, manifest.exercise("variables01"))
    assert state.is_unlocked(manifest, manifest.exercise("strings01"))


def test_second_exercise_locked_until_previous_completed(workspace: Path):
    manifest = load_manifest(workspace)
    state = State.load(workspace)
    assert not state.is_unlocked(manifest, manifest.exercise("variables02"))
    state.mark_done("variables01")
    assert state.is_unlocked(manifest, manifest.exercise("variables02"))


def test_topics_unlock_independently(workspace: Path):
    """别的课题进度不能解锁本课题的后续题。"""
    manifest = load_manifest(workspace)
    state = State.load(workspace)
    state.mark_done("strings01")
    assert not state.is_unlocked(manifest, manifest.exercise("variables02"))


def test_lock_message_points_to_first_pending_predecessor():
    manifest = three_exercise_manifest()
    state = in_memory_state({"t02"})  # 空洞：t01 没做，t02 做了
    exercise = manifest.exercise("t03")
    assert state.blocking_exercise(manifest, exercise).id == "t01"
    assert not state.is_unlocked(manifest, exercise)
    assert "t01" in state.lock_message(manifest, exercise)


def test_completed_exercise_always_accessible():
    """已完成的题即使前驱空洞也仍可访问。"""
    manifest = three_exercise_manifest()
    state = in_memory_state({"t03"})
    assert state.is_unlocked(manifest, manifest.exercise("t03"))
    assert state.lock_message(manifest, manifest.exercise("t03")) is None


def test_lock_message_none_when_unlocked():
    manifest = three_exercise_manifest()
    state = in_memory_state({"t01"})
    assert state.lock_message(manifest, manifest.exercise("t02")) is None


def test_first_pending_returns_unlocked_exercise(workspace: Path):
    """把 spec 5.1 的「first_pending 天然安全」证明固定成测试。"""
    manifest = load_manifest(workspace)
    state = State.load(workspace)
    pending = state.first_pending(manifest)
    assert pending is not None
    assert state.is_unlocked(manifest, pending)
