assert isinstance(total, float), "total 应该是 float，不能是字符串"
assert abs(total - 22.0) < 1e-9, f"总价应该是 3.50 + 6.00 + 12.50 = 22.0，而不是 {total}"
