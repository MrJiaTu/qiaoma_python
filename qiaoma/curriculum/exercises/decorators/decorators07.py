# ============================================================
# 装饰器 07 · functools.wraps 保名字
# ============================================================
# 【场景】装饰后函数的 __name__ 变成了 wrapper，排查问题很麻烦。
# 【任务】用 functools.wraps 保留原函数信息。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
import functools

def deco(func):
    def wrapper():
        return func()
    return wrapper  # 少了 @functools.wraps(func)

@deco
def pay():
    return "已支付"

name = pay.__name__
