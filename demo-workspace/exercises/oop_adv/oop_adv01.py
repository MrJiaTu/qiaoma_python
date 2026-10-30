# ============================================================
# 面向对象进阶 01 · 抽象支付接口
# ============================================================
# 【场景】收银台只认 pay 方法，不关心是哪种支付。Payment 基类应强制子类实现 pay。
# 【任务】修复 Payment 类，用 raise NotImplementedError 定义接口。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
class Payment:
    def pay(self, amount):
        pass  # 直接 pass 会被子类误当成可用实现

class CashPayment(Payment):
    pass

error = None
try:
    CashPayment().pay(10)
except NotImplementedError:
    error = "必须实现"
