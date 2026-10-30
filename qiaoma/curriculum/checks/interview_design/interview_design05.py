src = open("exercises/interview_design/interview_design05.py", encoding="utf-8").read()
assert "with self.lock" in src or "self.lock.acquire" in src, "判断+扣减必须在锁内"
inv = Inventory(3)
results = [inv.buy() for _ in range(5)]
assert results.count(True) == 3 and inv.stock == 0
