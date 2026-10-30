# ============================================================
# 装饰器 05 · 接口耗时统计
# ============================================================
# 【场景】性能组要记录接口耗时（秒），写进 elapsed 变量。
# 【任务】用 time 实现 timing 装饰器。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
import time

elapsed = None

def timing(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result  # 没计时
    return wrapper

@timing
def slow_api():
    time.sleep(0.05)
    return "ok"

slow_api()
