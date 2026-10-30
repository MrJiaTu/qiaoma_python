# ============================================================
# 线程与进程 06 · Event 发车信号
# ============================================================
# 【场景】检票完成（set）后，候车线程才出发（wait）。
# 【任务】修复代码：先 wait 再记录出发。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
import threading

departed = []
signal = threading.Event()

def wait_train():
    departed.append("出发")  # 没等信号

t = threading.Thread(target=wait_train)
t.start()
signal.set()
t.join()
