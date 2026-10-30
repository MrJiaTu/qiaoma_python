import queue
import threading

q = queue.Queue()
for i in range(3):
    q.put(f"订单{i}")

taken = []

def consume():
    while not q.empty():
        taken.append(q.get_nowait())

t = threading.Thread(target=consume)
t.start()
t.join()
count = len(taken)
