# ============================================================
# 装饰器 09 · 装饰器叠加顺序
# ============================================================
# 【场景】下单接口同时加日志和权限检查，注意叠加顺序。
# 【任务】修复装饰顺序：先进权限检查，再进日志。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
steps = []

def auth(func):
    def wrapper():
        steps.append("auth")
        return func()
    return wrapper

def log(func):
    def wrapper():
        steps.append("log")
        return func()
    return wrapper

@log
@auth
def order():
    steps.append("order")

order()
