assert sorted(intersection([1, 2, 2, 1], [2, 2])) == [2]
assert sorted(intersection([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]
assert intersection([1], [2]) == []
