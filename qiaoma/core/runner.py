"""判题运行器：在子进程中执行「题目代码 + 隐藏检查」。

题目文件中若仍存在「我还没做完」标记，判为 blocked；
否则在同一命名空间先后执行题目与检查，断言全部通过为 passed。
"""
from __future__ import annotations

import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from .manifest import Exercise

NOT_DONE_MARKER = "我还没做完"


def _has_not_done_marker(source: str) -> bool:
    """标记必须是形如 ``# 我还没做完`` 的注释行，题面注释中提到不算。"""
    for line in source.splitlines():
        stripped = line.strip()
        if stripped.startswith("#") and NOT_DONE_MARKER in stripped:
            return True
    return False

# 子进程驱动脚本：依次执行题目与检查，用退出码区分结果
_DRIVER_SOURCE = '''
import sys
import traceback

exercise_path, check_path = sys.argv[1], sys.argv[2]
namespace = {"__name__": "__qiaoma__"}


def run(path):
    with open(path, encoding="utf-8") as f:
        code = f.read()
    exec(compile(code, path, "exec"), namespace)


try:
    run(exercise_path)
    run(check_path)
except AssertionError as error:
    print(str(error) or "断言失败", file=sys.stderr)
    sys.exit(2)
except Exception:
    traceback.print_exc()
    sys.exit(3)
'''


@dataclass(frozen=True)
class CheckResult:
    """判题结果。status: passed / failed / blocked。"""

    status: str
    message: str

    @property
    def passed(self) -> bool:
        return self.status == "passed"


def run_check(
    workspace: Path,
    exercise: Exercise,
    timeout: float = 10.0,
) -> CheckResult:
    """运行一道题的隐藏检查，永不抛异常，统一返回 CheckResult。"""
    try:
        return _run_check(workspace, exercise, timeout)
    except Exception as error:  # 题目/检查文件缺失等意外也兜住
        return CheckResult("failed", f"判题出错：{error}")


def _run_check(
    workspace: Path,
    exercise: Exercise,
    timeout: float,
) -> CheckResult:
    source = exercise.path(workspace).read_text(encoding="utf-8")
    if _has_not_done_marker(source):
        return CheckResult(
            "blocked",
            "这道题还带着「我还没做完」标记：先修复代码，再删除标记所在行。",
        )

    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    try:
        proc = subprocess.run(
            [
                sys.executable,
                "-I",
                "-X",
                "utf8",  # 强制 UTF-8 模式：中文报错信息在 Windows 下不被 GBK 弄花
                "-c",
                _DRIVER_SOURCE,
                str(exercise.path(workspace)),
                str(exercise.check_path(workspace)),
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
            cwd=str(workspace),
            env=env,
        )
    except subprocess.TimeoutExpired:
        return CheckResult(
            "failed", f"执行超时（超过 {timeout:.0f} 秒），请检查代码里是否有死循环。"
        )

    if proc.returncode == 0:
        return CheckResult("passed", "全部检查通过！")
    detail = (proc.stderr or proc.stdout or "").strip()
    if proc.returncode == 2:
        return CheckResult("failed", f"检查未通过：{detail}" if detail else "检查未通过")
    return CheckResult("failed", f"运行时错误：\n{detail}" if detail else "运行时错误")
