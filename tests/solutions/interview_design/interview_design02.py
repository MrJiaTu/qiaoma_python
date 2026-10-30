class SlidingLimiter:
    def __init__(self, limit, window):
        self.limit = limit
        self.window = window
        self.timestamps = []

    def allow(self, now):
        while self.timestamps and self.timestamps[0] <= now - self.window:
            self.timestamps.pop(0)
        if len(self.timestamps) < self.limit:
            self.timestamps.append(now)
            return True
        return False
