# ============================================================
# 场景设计题 07 · 布隆过滤器（简版）
# ============================================================
# 【场景】缓存穿透防护：快速判断 URL 「可能存在/一定不存在」。
# 【要求】实现 BloomFilter 的 add/might_contain。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
class BloomFilter:
    def __init__(self, size=64):
        self.bits = [False] * size
        self.size = size

    def _hashes(self, item):
        return [hash(item) % self.size, hash(item + "#") % self.size]

    def add(self, item):
        pass  # 没置位

    def might_contain(self, item):
        return False  # 永远说不存在
