src = open("exercises/algo_array/algo_array10.py", encoding="utf-8").read()
assert src.count("for") <= 1, "要求一次遍历 O(n)，不要用双重循环"
assert max_profit([7, 1, 5, 3, 6, 4]) == 5
assert max_profit([7, 6, 4, 3, 1]) == 0
