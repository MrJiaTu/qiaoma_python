lines = open("duty.txt", encoding="utf-8").read().splitlines()
assert lines == ["早班：一切正常", "晚班：无异常"], f"早班记录被覆盖了：{lines}"
