events = []

class BikeLock:
    def __enter__(self):
        events.append("开锁")
        return self

    def __exit__(self, exc_type, exc, tb):
        events.append("落锁")

with BikeLock():
    events.append("骑行")
