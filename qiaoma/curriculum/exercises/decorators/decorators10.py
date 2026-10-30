# ============================================================
# 装饰器 10 · 类实现装饰器
# ============================================================
# 【场景】用类实现计数装饰器：记录函数被调用次数。
# 【任务】补全 CountCalls 类的 __call__。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)  # 没计数

@CountCalls
def say_hi():
    return "你好"

say_hi()
say_hi()
say_hi()
