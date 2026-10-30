"""reset / workspace 模块测试：题目重置与课程初始化。"""
from __future__ import annotations

from pathlib import Path

from qiaoma.core.manifest import load_manifest
from qiaoma.core.reset import reset_exercise
from qiaoma.core.workspace import find_workspace, init_workspace, packaged_curriculum


def test_packaged_curriculum_exists():
    root = packaged_curriculum()
    assert (root / "info.toml").is_file()
    assert (root / "exercises").is_dir()
    assert (root / "checks").is_dir()


def test_init_workspace_copies_curriculum(tmp_path: Path):
    target = tmp_path / "learn"
    init_workspace(target)
    assert (target / "info.toml").is_file()
    manifest = load_manifest(target)
    for ex in manifest.exercises:
        assert ex.path(target).is_file(), f"缺少题目文件 {ex.id}"
        assert ex.check_path(target).is_file(), f"缺少检查文件 {ex.id}"


def test_init_workspace_keeps_existing_state(tmp_path: Path):
    target = tmp_path / "learn"
    init_workspace(target)
    (target / "state.json").write_text('{"completed": ["a"]}', encoding="utf-8")
    init_workspace(target)
    assert '"completed"' in (target / "state.json").read_text(encoding="utf-8")


def test_reset_restores_original_code(tmp_path: Path):
    target = tmp_path / "learn"
    init_workspace(target)
    manifest = load_manifest(target)
    first = manifest.exercises[0]
    original = first.path(target).read_text(encoding="utf-8")

    first.path(target).write_text("# 被我改坏了\n", encoding="utf-8")
    reset_exercise(target, first)
    assert first.path(target).read_text(encoding="utf-8") == original


def test_find_workspace_detects_current_dir(tmp_path: Path):
    target = tmp_path / "learn"
    init_workspace(target)
    assert find_workspace(target) == target
    assert find_workspace(target / "exercises") == target


def test_find_workspace_returns_none_for_plain_dir(tmp_path: Path):
    assert find_workspace(tmp_path, fallback_home=tmp_path / "no-home") is None
