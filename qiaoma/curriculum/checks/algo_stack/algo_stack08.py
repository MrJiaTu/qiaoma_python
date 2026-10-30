src = open("exercises/algo_stack/algo_stack08.py", encoding="utf-8").read()
assert src.count("for") <= 1, "要求前缀和+哈希一次遍历"
assert subarray_sum([1, 1, 1], 2) == 2
assert subarray_sum([1, -1, 1, -1], 0) == 4
assert subarray_sum([1], 0) == 0
