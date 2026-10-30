# ============================================================
# 线程与进程 04 · 线程安全队列
# ============================================================
# 【场景】生产者放订单、消费者取订单，用 queue.Queue 传递。
# 【任务】修复消费者：从队列取出全部订单。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
import queue
import threading

q = queue.Queue()
for i in range(3):
    q.put(f"订单{i}")

taken = []

def consume():
    while not q.empty():
        taken.append(q.qsize())  # 取的是队列长度不是订单

t = threading.Thread(target=consume)
t.start()
t.join()
count = len(taken)
