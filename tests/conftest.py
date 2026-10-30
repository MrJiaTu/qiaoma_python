"""共享测试夹具：在临时目录中构造一个迷你课程工作区。"""
from __future__ import annotations

from pathlib import Path

import pytest

MINI_INFO_TOML = """\
[[topics]]
id = "variables"
name = "变量与类型"
track = "初级"
description = "从饭卡找零开始认识变量"

[[topics]]
id = "strings"
name = "字符串"
track = "初级"
description = "文本处理入门"

[[exercises]]
id = "variables01"
topic = "variables"
title = "饭卡找零"
hints = ["先算出总价", "再用减法求找零"]

[[exercises]]
id = "variables02"
topic = "variables"
title = "年龄计算"
hints = ["用当前年份减去出生年份"]

[[exercises]]
id = "strings01"
topic = "strings"
title = "打招呼"
hints = ["用加号拼接字符串"]
"""

PASSING_EXERCISE = """\
change = 100 - 35
"""

PASSING_CHECK = """\
assert change == 65, "找零应为 65 元"
"""

BLOCKED_EXERCISE = """\
# 我还没做完
change = 100 - 35
"""

FAILING_CHECK = """\
assert change == 999, "故意失败的检查"
"""


def make_workspace(root: Path) -> Path:
    """在 root 下构造一个包含两门课题的迷你工作区。"""
    ws = root / "workspace"
    (ws / "exercises" / "variables").mkdir(parents=True)
    (ws / "exercises" / "strings").mkdir(parents=True)
    (ws / "checks" / "variables").mkdir(parents=True)
    (ws / "checks" / "strings").mkdir(parents=True)

    (ws / "info.toml").write_text(MINI_INFO_TOML, encoding="utf-8")
    (ws / "exercises" / "variables" / "variables01.py").write_text(
        PASSING_EXERCISE, encoding="utf-8"
    )
    (ws / "exercises" / "variables" / "variables02.py").write_text(
        BLOCKED_EXERCISE, encoding="utf-8"
    )
    (ws / "exercises" / "strings" / "strings01.py").write_text(
        PASSING_EXERCISE, encoding="utf-8"
    )
    (ws / "checks" / "variables" / "variables01.py").write_text(
        PASSING_CHECK, encoding="utf-8"
    )
    (ws / "checks" / "variables" / "variables02.py").write_text(
        PASSING_CHECK, encoding="utf-8"
    )
    (ws / "checks" / "strings" / "strings01.py").write_text(
        FAILING_CHECK, encoding="utf-8"
    )
    return ws


@pytest.fixture
def workspace(tmp_path: Path) -> Path:
    return make_workspace(tmp_path)
