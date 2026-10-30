a = [0, 1, 0, 3, 12]
move_zeroes(a)
assert a == [1, 3, 12, 0, 0], f"0 要移到最后：{a}"
b = [0, 0, 1]
move_zeroes(b)
assert b == [1, 0, 0]
