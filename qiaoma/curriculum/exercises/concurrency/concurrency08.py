# ============================================================
# 线程与进程 08 · 条件变量叫号
# ============================================================
# 【场景】取餐屏：没有准备好的餐时等待，notify 后取餐。
# 【任务】用 Condition 实现等待与通知。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
import threading

cond = threading.Condition()
ready = False
picked = []

def customer():
    global ready
    with cond:
        picked.append("取餐")  # 没等待 ready

def kitchen():
    global ready
    with cond:
        ready = True
        cond.notify()

src_check = None
t = threading.Thread(target=customer)
t.start()
kitchen()
t.join()
