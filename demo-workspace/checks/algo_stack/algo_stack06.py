assert top_k([1, 1, 1, 2, 2, 3], 2) == [1, 2]
assert top_k([5], 1) == [5]
assert len(top_k([1, 1, 2, 2, 3], 2)) == 2
