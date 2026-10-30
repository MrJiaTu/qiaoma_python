# ============================================================
# 类型注解与dataclass 09 · post_init 校验
# ============================================================
# 【场景】订单金额不能为负，用 __post_init__ 校验。
# 【任务】实现 __post_init__，金额小于 0 时抛 ValueError。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
from dataclasses import dataclass

@dataclass
class Order:
    amount: float
    # 缺少 __post_init__

caught = False
try:
    Order(-5)
except ValueError:
    caught = True
