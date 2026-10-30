assert isinstance(balance, (int, float)), "balance 应该是一个数字"
assert abs(balance - 37.5) < 1e-9, f"余额应该是 50 - 12.5 = 37.5，而不是 {balance}"
