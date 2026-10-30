# ============================================================
# 类型注解与dataclass 03 · 总价方法
# ============================================================
# 【场景】Order 要能算总价：菜价 + 配送费。
# 【任务】给 dataclass 加 total 方法。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
from dataclasses import dataclass

@dataclass
class Order:
    dish: str
    price: float
    delivery_fee: float = 3.0

    def total(self):
        return self.price  # 配送费没加

order = Order("米线", 15.0)
pay = order.total()
