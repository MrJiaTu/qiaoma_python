# ============================================================
# 类型注解与dataclass 05 · 只读订单号
# ============================================================
# 【场景】订单号生成后不允许修改，用 frozen。
# 【任务】把 Order 设为不可变。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
from dataclasses import dataclass

@dataclass
class Order:
    order_no: str
    amount: float

order = Order("DD001", 25.0)
blocked = False
try:
    order.order_no = "DD999"
except Exception:
    blocked = True
