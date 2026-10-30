# ============================================================
# 类型注解与dataclass 06 · 可变默认用 field
# ============================================================
# 【场景】订单可以带多张优惠券，默认空列表要用 field(default_factory)。
# 【任务】修复 coupons 字段的默认值写法。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
from dataclasses import dataclass

@dataclass
class Order:
    dish: str
    coupons: list = []  # 可变默认值会报错

order = Order("盖饭")
assert order.coupons == []
