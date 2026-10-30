src = open("exercises/algo_stack/algo_stack09.py", encoding="utf-8").read()
assert "max(nums[i:i + k])" not in src, "请用单调队列而不是重复 max"
assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
assert max_sliding_window([1], 1) == [1]
