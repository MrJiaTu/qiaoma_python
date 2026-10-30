sl = SlidingLimiter(2, 3)
assert sl.allow(0) is True
assert sl.allow(1) is True
assert sl.allow(2) is False, "窗口内已 2 次"
assert sl.allow(3) is True, "0 秒的请求已滑出窗口"
assert sl.allow(4) is True, "1 秒的请求也滑出窗口"
assert sl.allow(5) is False, "3、4 秒的两次仍在窗口内"
assert sl.allow(6) is True
