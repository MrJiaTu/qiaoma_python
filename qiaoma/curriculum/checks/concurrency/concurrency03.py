src = open("exercises/concurrency/concurrency03.py", encoding="utf-8").read()
assert "with lock" in src or "lock.acquire" in src, "要用锁保护扣票操作"
assert tickets == 0, f"两线程各抢 50 张后应为 0：{tickets}"
