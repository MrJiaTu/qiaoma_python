src = open("exercises/concurrency/concurrency08.py", encoding="utf-8").read()
assert "cond.wait" in src, "顾客要用 cond.wait_for/cond.wait 等待"
assert picked == ["取餐"]
