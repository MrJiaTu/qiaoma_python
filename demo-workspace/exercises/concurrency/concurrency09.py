# ============================================================
# 线程与进程 09 · 线程池并行下载
# ============================================================
# 【场景】批量下载 5 张图，用 ThreadPoolExecutor 并发执行。
# 【任务】用 pool.map 并行执行 download。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
from concurrent.futures import ThreadPoolExecutor

def download(n):
    return f"图{n}"

with ThreadPoolExecutor(max_workers=2) as pool:
    results = [download(n) for n in range(1, 6)]  # 没用上线程池
