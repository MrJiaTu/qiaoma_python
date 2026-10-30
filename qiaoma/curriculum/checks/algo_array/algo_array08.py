src = open("exercises/algo_array/algo_array08.py", encoding="utf-8").read()
assert "sort" not in src, "请用从后往前的双指针，而不是排序"
a = [1, 2, 3, 0, 0, 0]
assert merge(a, [2, 5, 6]) == [1, 2, 2, 3, 5, 6]
assert merge([2, 0], [1]) == [1, 2]
assert merge([0], []) == [0]
