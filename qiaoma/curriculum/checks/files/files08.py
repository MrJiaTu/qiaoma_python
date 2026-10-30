lines = open("stars.txt", encoding="utf-8").read().splitlines()
assert lines == ["张三", "李四", "王五"], f"每人要占一行：{lines}"
