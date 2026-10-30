assert isinstance(balance, (int, float)), "balance 应该是一个数字"
assert balance == 64, f"最终余额应该是 20 + 50 - 2×3 = 64，而不是 {balance}"
