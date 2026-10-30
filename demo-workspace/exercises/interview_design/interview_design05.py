# ============================================================
# 场景设计题 05 · 秒杀库存扣减
# ============================================================
# 【场景】库存 100 件，并发请求扣减，绝不能超卖。
# 【要求】实现 Inventory.buy()，库存不足返回 False。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
import threading

class Inventory:
    def __init__(self, stock):
        self.stock = stock
        self.lock = threading.Lock()

    def buy(self):
        if self.stock > 0:
            self.stock -= 1
            return True  # 没加锁，并发会超卖
        return False
