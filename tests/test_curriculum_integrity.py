"""课程完整性：28 课题 × 10 题，文件镜像齐全。"""
from __future__ import annotations

from pathlib import Path

from qiaoma.core.manifest import load_manifest
from qiaoma.core.workspace import packaged_curriculum


def test_curriculum_shape_is_28_topics_x_10():
    manifest = load_manifest(packaged_curriculum())
    assert len(manifest.topics) == 28, f"应有 28 个课题：{len(manifest.topics)}"
    assert len(manifest.exercises) == 280, f"应有 280 道题：{len(manifest.exercises)}"
    for topic in manifest.topics:
        exercises = manifest.exercises_for(topic.id)
        assert len(exercises) == 10, f"课题 {topic.id} 应含 10 题：{len(exercises)}"
        assert topic.track in ("初级", "中级", "算法", "面试"), topic.track


def test_tracks_follow_plan():
    manifest = load_manifest(packaged_curriculum())
    tracks = {}
    for topic in manifest.topics:
        tracks.setdefault(topic.track, []).append(topic.id)
    assert len(tracks["初级"]) == 12
    assert len(tracks["中级"]) == 8
    assert len(tracks["算法"]) == 5
    assert len(tracks["面试"]) == 3


def test_every_exercise_and_check_file_exists():
    root = packaged_curriculum()
    manifest = load_manifest(root)
    for exercise in manifest.exercises:
        assert exercise.path(root).is_file(), f"缺题目文件：{exercise.id}"
        assert exercise.check_path(root).is_file(), f"缺检查文件：{exercise.id}"


def test_every_exercise_has_two_hints():
    manifest = load_manifest(packaged_curriculum())
    for exercise in manifest.exercises:
        assert len(exercise.hints) == 2, f"{exercise.id} 应有 2 条提示"
