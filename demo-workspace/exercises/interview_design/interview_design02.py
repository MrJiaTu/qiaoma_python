# ============================================================
# 场景设计题 02 · 滑动窗口限流
# ============================================================
# 【场景】更精细的限流：最近 window 时间内最多 limit 次（记录时间戳）。
# 【要求】实现 SlidingLimiter.allow(now)。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
class SlidingLimiter:
    def __init__(self, limit, window):
        self.limit = limit
        self.window = window
        self.timestamps = []

    def allow(self, now):
        return len(self.timestamps) <= self.limit  # 没清理过期时间戳
