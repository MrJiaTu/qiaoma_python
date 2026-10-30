# ============================================================
# 装饰器 06 · 带参装饰器
# ============================================================
# 【场景】重试装饰器 @retry(3)：失败自动重试，次数可配置。
# 【任务】实现三层嵌套的 retry 装饰器。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)  # 没有重试
        return wrapper
    return decorator

attempts = []

@retry(3)
def unstable():
    attempts.append(1)
    if len(attempts) < 3:
        raise ConnectionError("网络抖动")
    return "成功"

result = unstable()
