assert len(winners) == 2 and len(set(winners)) == 2, f"要两名不重复的幸运儿：{winners}"
assert all(w in numbers for w in winners), f"号码必须在抽奖池里：{winners}"
