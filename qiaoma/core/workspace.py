"""工作区：初始化学习目录、定位当前工作区、访问打包课程。"""
from __future__ import annotations

import shutil
from pathlib import Path
from typing import Optional

DEFAULT_HOME_NAME = ".qiaoma"


def packaged_curriculum() -> Path:
    """随包发布的课程目录（info.toml + exercises/ + checks/）。"""
    return Path(__file__).resolve().parent.parent / "curriculum"


def init_workspace(path: Path) -> Path:
    """把打包课程复制到学习工作区。

    已存在的文件一律不覆盖：重复执行 init 不会丢失学员的
    做题进度（state.json）或已编辑的题目文件，只会补齐新题。
    """
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    source = packaged_curriculum()

    def copy_preserving(src: Path, dst: Path) -> None:
        if src.is_dir():
            dst.mkdir(exist_ok=True)
            for child in src.iterdir():
                copy_preserving(child, dst / child.name)
        elif not dst.exists():
            shutil.copyfile(src, dst)

    copy_preserving(source / "info.toml", path / "info.toml")
    for folder in ("exercises", "checks"):
        copy_preserving(source / folder, path / folder)
    return path


def _is_workspace(path: Path) -> bool:
    return (path / "info.toml").is_file() and (path / "exercises").is_dir()


def find_workspace(
    start: Optional[Path] = None,
    fallback_home: Optional[Path] = None,
) -> Optional[Path]:
    """从 start 向上查找工作区；找不到再看默认主目录 ``~/.qiaoma``。"""
    current = Path(start or Path.cwd()).resolve()
    for candidate in [current, *current.parents]:
        if _is_workspace(candidate):
            return candidate
    home = Path(fallback_home) if fallback_home else Path.home() / DEFAULT_HOME_NAME
    if _is_workspace(home):
        return home
    return None
