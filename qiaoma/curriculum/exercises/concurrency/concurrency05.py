# ============================================================
# 线程与进程 05 · 信号量限流下载
# ============================================================
# 【场景】下载站最多同时 2 个连接，用 Semaphore 控制。
# 【任务】修复 download：进出临界区时获取/释放信号量。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
import threading

sem = threading.Semaphore(2)
active = 0
peak = 0
peak_lock = threading.Lock()

def download(_i):
    global active, peak
    active += 1
    with peak_lock:
        peak = max(peak, active)
    active -= 1  # 没用信号量

threads = [threading.Thread(target=download, args=(i,)) for i in range(6)]
[t.start() for t in threads]
[t.join() for t in threads]
