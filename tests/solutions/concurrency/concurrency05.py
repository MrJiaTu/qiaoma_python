import threading

sem = threading.Semaphore(2)
active = 0
peak = 0
peak_lock = threading.Lock()

def download(_i):
    global active, peak
    with sem:
        active += 1
        with peak_lock:
            peak = max(peak, active)
        active -= 1

threads = [threading.Thread(target=download, args=(i,)) for i in range(6)]
[t.start() for t in threads]
[t.join() for t in threads]
