# ============================================================
# 异常处理 02 · 银行取款余额不足
# ============================================================
# 【场景】取款函数在余额不足时要主动抛出 ValueError 提示柜员。
# 【任务】修复 withdraw，让它在余额不足时 raise。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
def withdraw(balance, amount):
    if amount > balance:
        print("余额不足")  # 只打印不抛异常
    return balance - amount

error = None
try:
    withdraw(100, 500)
except ValueError as e:
    error = str(e)
