# ============================================================
# 线程与进程 07 · 线程局部数据
# ============================================================
# 【场景】每个请求线程有自己的用户，用 threading.local 隔离。
# 【任务】修复代码：用 local 存用户名，互不干扰。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
import threading

local = threading.local()
seen = {}

def handle(name):
    local.user = name
    seen[name] = local.user

t1 = threading.Thread(target=handle, args=("张三",))
t2 = threading.Thread(target=handle, args=("李四",))
t1.start(); t2.start(); t1.join(); t2.join()
