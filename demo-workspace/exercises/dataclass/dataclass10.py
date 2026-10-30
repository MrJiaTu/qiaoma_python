# ============================================================
# 类型注解与dataclass 10 · asdict 导出接口
# ============================================================
# 【场景】订单要序列化成字典传给前端。
# 【任务】用 dataclasses.asdict 导出。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
from dataclasses import dataclass

@dataclass
class Order:
    dish: str
    price: float

order = Order("酸辣粉", 12.0)
payload = {"dish": order.dish}  # 手动拼漏了 price
