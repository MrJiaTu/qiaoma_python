"""学习进度：持久化到工作区 state.json。"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Optional, Set, Tuple

from .manifest import Exercise, Manifest


class State:
    """记录已完成题目与当前题目，保存为 ``state.json``。"""

    def __init__(
        self,
        workspace: Path,
        completed: Set[str],
        current_id: Optional[str],
    ) -> None:
        self._workspace = Path(workspace)
        self.completed = completed
        self.current_id = current_id

    # ---- 持久化 ----

    @classmethod
    def load(cls, workspace: Path) -> "State":
        state_path = Path(workspace) / "state.json"
        if state_path.is_file():
            data = json.loads(state_path.read_text(encoding="utf-8"))
            return cls(
                workspace,
                completed=set(data.get("completed", [])),
                current_id=data.get("current"),
            )
        return cls(workspace, completed=set(), current_id=None)

    def save(self) -> None:
        state_path = self._workspace / "state.json"
        payload = {
            "completed": sorted(self.completed),
            "current": self.current_id,
        }
        state_path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    # ---- 进度操作 ----

    def is_done(self, exercise_id: str) -> bool:
        return exercise_id in self.completed

    def mark_done(self, exercise_id: str) -> None:
        self.completed.add(exercise_id)

    def set_current(self, exercise_id: str) -> None:
        self.current_id = exercise_id

    # ---- 顺序解锁 ----

    def blocking_exercise(
        self, manifest: Manifest, exercise: Exercise
    ) -> Optional[Exercise]:
        """返回该题之前第一道未完成的同课题题目；无阻塞返回 None。

        指向「第一个未完成的前驱」而不是「物理前一个题目」，
        这样 completed 有空洞时提示仍指向学员真正该做的题。
        """
        siblings = manifest.exercises_for(exercise.topic)
        ids = [ex.id for ex in siblings]
        try:
            index = ids.index(exercise.id)
        except ValueError:
            return None  # 清单外的题目 id
        for prev in siblings[:index]:
            if not self.is_done(prev.id):
                return prev
        return None

    def is_unlocked(self, manifest: Manifest, exercise: Exercise) -> bool:
        """课题内顺序解锁判定；已完成的题始终可访问。"""
        return self.is_done(exercise.id) or (
            self.blocking_exercise(manifest, exercise) is None
        )

    def lock_message(self, manifest: Manifest, exercise: Exercise) -> Optional[str]:
        """未解锁时返回可直接展示的中文提示；可访问时返回 None。

        TUI 与 CLI 共用这句话，避免两处文案漂移。
        """
        if self.is_done(exercise.id):
            return None
        blocking = self.blocking_exercise(manifest, exercise)
        if blocking is None:
            return None
        return f"🔒 该题未解锁：先完成 {blocking.id} {blocking.title}"

    # ---- 题目导航 ----

    def first_pending(self, manifest: Manifest) -> Optional[Exercise]:
        """按课程顺序返回第一道未完成的题目；全部完成返回 None。"""
        for ex in manifest.exercises:
            if not self.is_done(ex.id):
                return ex
        return None

    def next_after(self, exercise_id: str, manifest: Manifest) -> Optional[Exercise]:
        """返回指定题目之后的下一道题；已是最后一题返回 None。"""
        ids = [ex.id for ex in manifest.exercises]
        try:
            index = ids.index(exercise_id)
        except ValueError:
            return None
        if index + 1 < len(ids):
            return manifest.exercises[index + 1]
        return None

    def topic_progress(self, manifest: Manifest, topic_id: str) -> Tuple[int, int]:
        """返回某课题 (已完成数, 总题数)。"""
        exercises = manifest.exercises_for(topic_id)
        done = sum(1 for ex in exercises if self.is_done(ex.id))
        return done, len(exercises)
