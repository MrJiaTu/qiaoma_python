src = open("exercises/concurrency/concurrency06.py", encoding="utf-8").read()
assert "signal.wait()" in src, "乘客要等发车信号 signal.wait()"
assert departed == ["出发"]
