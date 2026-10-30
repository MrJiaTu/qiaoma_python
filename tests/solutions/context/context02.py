events = []

class BikeLock:
    def __enter__(self):
        events.append("开锁")
        return self

    def __exit__(self, exc_type, exc, tb):
        events.append("落锁")

try:
    with BikeLock():
        raise ValueError("摔车了")
except ValueError:
    pass
