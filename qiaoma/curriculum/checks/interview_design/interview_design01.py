rl = RateLimiter(2)
assert rl.allow(0) is True
assert rl.allow(0) is True
assert rl.allow(0) is False, "同一秒第三次应拒绝"
assert rl.allow(1) is True, "新的一秒窗口应重置"
assert rl.allow(1) is True
assert rl.allow(1) is False
