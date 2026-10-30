import time

elapsed = None

def timing(func):
    def wrapper(*args, **kwargs):
        global elapsed
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        return result
    return wrapper

@timing
def slow_api():
    time.sleep(0.05)
    return "ok"

slow_api()
