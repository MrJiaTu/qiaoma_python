got = permute([1, 2, 3])
assert len(got) == 6
assert sorted(map(tuple, got)) == sorted([(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)])
assert permute([1]) == [[1]]
