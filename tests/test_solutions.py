"""参考解答套件：确保每道题都存在可通过的解答。

这是课程的「可解性」保险：tests/solutions 下的每份解答
替换进工作区后必须通过对应的隐藏检查。
"""
from __future__ import annotations

from pathlib import Path

from qiaoma.core.manifest import load_manifest
from qiaoma.core.runner import run_check
from qiaoma.core.workspace import init_workspace

SOLUTION_ROOT = Path(__file__).parent / "solutions"


def test_reference_solutions_pass_all_checks(tmp_path: Path):
    workspace = init_workspace(tmp_path / "ws")
    manifest = load_manifest(workspace)
    checked = 0
    for exercise in manifest.exercises:
        solution = SOLUTION_ROOT / exercise.topic / f"{exercise.id}.py"
        if not solution.is_file():
            continue  # 课题还没写到，由完整性测试兜底
        exercise.path(workspace).write_text(
            solution.read_text(encoding="utf-8"), encoding="utf-8"
        )
        result = run_check(workspace, exercise, timeout=15)
        assert result.passed, f"{exercise.id} 参考解答未通过：{result.message}"
        checked += 1
    assert checked > 0, "一份参考解答都没有，课程生成脚本没跑？"


def test_every_exercise_has_solution(tmp_path: Path):
    """Phase 6 完成标志：280 道题全部有参考解答。"""
    workspace = init_workspace(tmp_path / "ws")
    manifest = load_manifest(workspace)
    missing = [
        exercise.id
        for exercise in manifest.exercises
        if not (SOLUTION_ROOT / exercise.topic / f"{exercise.id}.py").is_file()
    ]
    assert not missing, f"缺少参考解答（{len(missing)} 题）：{missing[:10]}..."
