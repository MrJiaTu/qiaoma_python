src = open("exercises/algo_stack/algo_stack07.py", encoding="utf-8").read()
assert src.count("for") <= 1, "要求单调栈一次遍历 O(n)"
assert next_greater([2, 1, 2, 4, 3]) == [4, 2, 4, -1, -1]
assert next_greater([3, 2, 1]) == [-1, -1, -1]
