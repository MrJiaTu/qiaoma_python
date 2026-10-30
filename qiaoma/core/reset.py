"""题目重置：从打包课程恢复题目文件的原始内容。"""
from __future__ import annotations

import shutil
from pathlib import Path

from .manifest import Exercise
from .workspace import packaged_curriculum


def reset_exercise(workspace: Path, exercise: Exercise) -> None:
    """用打包课程中的原始题目覆盖学员工作区里的题目文件。"""
    source = (
        packaged_curriculum() / "exercises" / exercise.topic / f"{exercise.id}.py"
    )
    target = exercise.path(workspace)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
