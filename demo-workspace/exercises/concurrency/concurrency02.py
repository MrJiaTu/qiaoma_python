# ============================================================
# 线程与进程 02 · join 等待完成
# ============================================================
# 【场景】汇总前必须等所有爬虫线程跑完。
# 【任务】修复代码：在主线程里 join 每个线程。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
import threading

pages = []

def crawl(name):
    pages.append(name)

threads = [threading.Thread(target=crawl, args=(f"页{i}",)) for i in range(3)]
for t in threads:
    t.start()
# 少了 join
count = len(pages)
