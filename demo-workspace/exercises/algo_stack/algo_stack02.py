# ============================================================
# 栈、队列与哈希表 02 · 最小栈
# ============================================================
# 【题目】设计支持 O(1) 取最小值的栈：push、pop、get_min。
# 【要求】补全 MinStack 的 get_min。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
class MinStack:
    def __init__(self):
        self.data = []
        self.mins = []

    def push(self, x):
        self.data.append(x)
        if not self.mins or x <= self.mins[-1]:
            self.mins.append(x)

    def pop(self):
        x = self.data.pop()
        if self.mins and x == self.mins[-1]:
            self.mins.pop()
        return x

    def get_min(self):
        return min(self.data)  # O(n)，不是 O(1)

s = MinStack()
for v in [3, 1, 2]:
    s.push(v)
m1 = s.get_min()
s.pop()
s.pop()
m2 = s.get_min()
