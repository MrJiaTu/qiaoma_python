import threading

tickets = 100
lock = threading.Lock()

def grab():
    global tickets
    for _ in range(50):
        with lock:
            tickets -= 1

t1 = threading.Thread(target=grab)
t2 = threading.Thread(target=grab)
t1.start(); t2.start()
t1.join(); t2.join()
