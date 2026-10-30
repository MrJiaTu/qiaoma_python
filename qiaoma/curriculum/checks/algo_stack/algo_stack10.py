src = open("exercises/algo_stack/algo_stack10.py", encoding="utf-8").read()
assert src.count("for") <= 1, "要求哈希一次遍历"
assert has_pair_with_diff([10, 3, 5, 7], 2) is True
assert has_pair_with_diff([1, 2, 3], 5) is False
assert has_pair_with_diff([1, 1], 0) is True
