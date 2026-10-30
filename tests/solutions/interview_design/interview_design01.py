class RateLimiter:
    def __init__(self, limit):
        self.limit = limit
        self.window_start = 0
        self.count = 0

    def allow(self, now):
        if now != self.window_start:
            self.window_start = now
            self.count = 0
        self.count += 1
        return self.count <= self.limit
