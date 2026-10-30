import threading

departed = []
signal = threading.Event()

def wait_train():
    signal.wait()
    departed.append("出发")

t = threading.Thread(target=wait_train)
t.start()
signal.set()
t.join()
