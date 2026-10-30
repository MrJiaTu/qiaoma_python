from contextlib import suppress
assert status == "忽略"
src = open("exercises/context/context05.py", encoding="utf-8").read()
assert "suppress(" in src, "要用 with suppress(...) 重写，而不是 try/except"
