src = open("exercises/algo_stack/algo_stack02.py", encoding="utf-8").read()
assert "min(self.data)" not in src, "要用辅助栈 mins 实现 O(1)"
assert m1 == 1 and m2 == 3, f"最小值应随弹出更新：{m1}/{m2}"
