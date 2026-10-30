# ============================================================
# 线程与进程 03 · 锁保护余票
# ============================================================
# 【场景】两个抢票线程同时扣减余票，不加锁会超卖。
# 【任务】用 threading.Lock 保护扣票操作。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
import threading

tickets = 100

def grab():
    global tickets
    for _ in range(50):
        tickets -= 1  # 没加锁

t1 = threading.Thread(target=grab)
t2 = threading.Thread(target=grab)
t1.start(); t2.start()
t1.join(); t2.join()
