src = open("exercises/algo_dp/algo_dp01.py", encoding="utf-8").read()
assert "cache" in src or "memo" in src or "lru_cache" in src or "dp" in src, "要用记忆化或动态规划"
assert fib(10) == 55
assert fib(0) == 0
assert fib(1) == 1
assert fib(50) == 12586269025
