# ============================================================
# 上下文管理器 03 · contextmanager 生成器版
# ============================================================
# 【场景】用 contextlib.contextmanager 写轻量上下文：进入打印开工，退出打印收工。
# 【任务】实现 work_session 生成器。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
from contextlib import contextmanager

events = []

@contextmanager
def work_session():
    events.append("开工")
    # 少了 yield 和收尾

with work_session():
    events.append("干活")
