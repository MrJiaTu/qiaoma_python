src = open("exercises/algo_array/algo_array03.py", encoding="utf-8").read()
assert "while" in src or ("left" in src and "right" in src), "要用左右双指针而不是双重循环"
assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert max_area([1, 1]) == 1
