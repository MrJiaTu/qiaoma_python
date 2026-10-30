# ============================================================
# 大厂高频手撕题 01 · LRU 缓存
# ============================================================
# 【题目】设计容量为 capacity 的 LRU：get 命中则提升为最新，put 超容量淘汰最久未用。
# 【要求】用保序字典（如 OrderedDict）实现 LRUCache。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

    def get(self, key):
        return self.cache.get(key, -1)  # 命中没提升新鲜度

    def put(self, key, value):
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem()  # 没淘汰最久未用
