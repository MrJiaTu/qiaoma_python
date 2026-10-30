got = combination_sum([2, 3, 6, 7], 7)
assert sorted(map(tuple, got)) == [(2, 2, 3), (7,)], f"结果不对：{got}"
assert combination_sum([2], 1) == []
