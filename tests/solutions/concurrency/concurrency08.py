import threading

cond = threading.Condition()
ready = False
picked = []

def customer():
    global ready
    with cond:
        cond.wait_for(lambda: ready)
        picked.append("取餐")

def kitchen():
    global ready
    with cond:
        ready = True
        cond.notify()

t = threading.Thread(target=customer)
t.start()
kitchen()
t.join()
