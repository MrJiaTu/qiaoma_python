# ============================================================
# 异常处理 07 · 自定义余额异常
# ============================================================
# 【场景】支付系统要定义自己的 InsufficientBalanceError 异常类型。
# 【任务】修复代码：定义自定义异常并在余额不足时抛出。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
class InsufficientBalanceError(Exception):
    pass

def pay(balance, price):
    if price > balance:
        raise ValueError("不够")  # 应该抛自定义异常
    return balance - price

caught = None
try:
    pay(10, 25)
except InsufficientBalanceError:
    caught = "余额不足"
