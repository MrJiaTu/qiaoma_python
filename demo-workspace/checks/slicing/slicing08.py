assert prices == [3.5, 6.0, 12.5], f"清洗后应为 [3.5, 6.0, 12.5]：{prices}"
assert all(isinstance(p, float) for p in prices)
