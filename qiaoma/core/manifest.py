"""课程清单：解析工作区的 info.toml，定义课题顺序与题目元数据。

info.toml 结构::

    [[topics]]
    id = "variables"
    name = "变量与类型"
    track = "初级"
    description = "..."

    [[exercises]]
    id = "variables01"
    topic = "variables"
    title = "饭卡找零"
    hints = ["提示一", "提示二"]

题目文件与检查文件按镜像路径存放：
``exercises/<topic>/<id>.py`` 对应 ``checks/<topic>/<id>.py``。
"""
from __future__ import annotations

import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional

if sys.version_info >= (3, 11):
    import tomllib
else:  # pragma: no cover - 3.10 回退
    import tomli as tomllib


@dataclass(frozen=True)
class Topic:
    """一门课题，例如「变量与类型」。"""

    id: str
    name: str
    track: str = ""
    description: str = ""


@dataclass(frozen=True)
class Exercise:
    """一道练习题。"""

    id: str
    topic: str
    title: str = ""
    hints: List[str] = field(default_factory=list)

    def path(self, workspace: Path) -> Path:
        """学员可编辑的题目文件路径。"""
        return workspace / "exercises" / self.topic / f"{self.id}.py"

    def check_path(self, workspace: Path) -> Path:
        """隐藏检查文件路径（与题目文件镜像）。"""
        return workspace / "checks" / self.topic / f"{self.id}.py"


@dataclass
class Manifest:
    """整个课程的清单。"""

    topics: List[Topic]
    exercises: List[Exercise]

    def exercise(self, exercise_id: str) -> Exercise:
        for ex in self.exercises:
            if ex.id == exercise_id:
                return ex
        raise KeyError(f"找不到题目：{exercise_id}")

    def exercises_for(self, topic_id: str) -> List[Exercise]:
        return [ex for ex in self.exercises if ex.topic == topic_id]


def load_manifest(workspace: Path) -> Manifest:
    """读取工作区 info.toml 构造清单；文件不存在时抛 FileNotFoundError。"""
    info_path = Path(workspace) / "info.toml"
    if not info_path.is_file():
        raise FileNotFoundError(f"不是敲码工作区（缺少 info.toml）：{workspace}")
    data = tomllib.loads(info_path.read_text(encoding="utf-8"))
    topics = [Topic(**entry) for entry in data.get("topics", [])]
    exercises = [Exercise(**entry) for entry in data.get("exercises", [])]
    return Manifest(topics=topics, exercises=exercises)
