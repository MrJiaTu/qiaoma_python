assert isinstance(shipping, (int, float)), "shipping 应该是一个数字"
assert abs(shipping - 14.9) < 1e-9, f"运费应该是 8 + 2.3×3 = 14.9，而不是 {shipping}"
