src = open("exercises/interview_coding/interview_coding05.py", encoding="utf-8").read()
assert "while" in src, "要用二分/迭代的快速幂"
assert my_pow(2, 10) == 1024
assert abs(my_pow(2, -2) - 0.25) < 1e-9
assert my_pow(3, 0) == 1
