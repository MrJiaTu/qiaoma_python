lb = Leaderboard()
lb.update("张三", 80)
lb.update("李四", 95)
lb.update("王五", 90)
lb.update("李四", 99)
assert lb.top_k(2) == ["李四", "王五"]
assert lb.top_k(1) == ["李四"]
lb.update("赵六", 90)
assert lb.top_k(3) == ["李四", "王五", "赵六"], "同分按名字字典序"
