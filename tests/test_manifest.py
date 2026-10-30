"""manifest 模块测试：info.toml 解析与题目定位。"""
from __future__ import annotations

from pathlib import Path

import pytest

from qiaoma.core.manifest import load_manifest


def test_loads_topics_in_order(workspace: Path):
    manifest = load_manifest(workspace)
    assert [t.id for t in manifest.topics] == ["variables", "strings"]
    assert manifest.topics[0].name == "变量与类型"
    assert manifest.topics[0].track == "初级"


def test_loads_exercises_in_order(workspace: Path):
    manifest = load_manifest(workspace)
    assert [e.id for e in manifest.exercises] == [
        "variables01",
        "variables02",
        "strings01",
    ]


def test_exercise_lookup_by_id(workspace: Path):
    manifest = load_manifest(workspace)
    ex = manifest.exercise("variables01")
    assert ex.title == "饭卡找零"
    assert ex.hints == ["先算出总价", "再用减法求找零"]


def test_exercise_lookup_missing_raises(workspace: Path):
    manifest = load_manifest(workspace)
    with pytest.raises(KeyError):
        manifest.exercise("不存在")


def test_exercises_for_topic(workspace: Path):
    manifest = load_manifest(workspace)
    exs = manifest.exercises_for("variables")
    assert [e.id for e in exs] == ["variables01", "variables02"]


def test_exercise_paths_mirror_checks(workspace: Path):
    manifest = load_manifest(workspace)
    ex = manifest.exercise("variables01")
    assert ex.path(workspace) == (
        workspace / "exercises" / "variables" / "variables01.py"
    )
    assert ex.check_path(workspace) == (
        workspace / "checks" / "variables" / "variables01.py"
    )


def test_missing_info_toml_raises(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        load_manifest(tmp_path)
