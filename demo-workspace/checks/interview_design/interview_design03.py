s = Shortener()
codes = [s.encode(f"https://example.com/{i}") for i in range(10)]
assert len(set(codes)) == 10
assert all(s.decode(c) == f"https://example.com/{i}" for i, c in enumerate(codes))
assert codes[9] == "a", "计数到 10 时 62 进制短码应是 a"
assert s.decode("不存在") is None
