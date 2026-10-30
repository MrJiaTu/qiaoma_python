# ============================================================
# 面向对象进阶 10 · 只读余额属性
# ============================================================
# 【场景】Account 的 balance 只允许读不允许直接改。
# 【任务】用 @property 实现只读 balance。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
class Account:
    def __init__(self, balance):
        self._balance = balance

    def balance(self):
        return self._balance  # 没加 @property

acc = Account(88)
value = acc.balance
