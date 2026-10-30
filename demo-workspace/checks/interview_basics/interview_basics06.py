assert answer == "不可以", "可变对象不可哈希，不能做键"
assert ok is False
assert {(1, 2): "值"}[(1, 2)] == "值"
