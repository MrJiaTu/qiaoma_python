# ============================================================
# 场景设计题 01 · 固定窗口限流器
# ============================================================
# 【场景】接口每秒最多放行 limit 次请求，超出的拒绝。
# 【要求】实现 RateLimiter.allow()（用传入的逻辑时钟 now）。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
class RateLimiter:
    def __init__(self, limit):
        self.limit = limit
        self.window_start = 0
        self.count = 0

    def allow(self, now):
        self.count += 1
        return self.count <= self.limit  # 窗口没滚动
