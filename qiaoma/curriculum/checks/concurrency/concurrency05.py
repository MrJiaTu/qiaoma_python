src = open("exercises/concurrency/concurrency05.py", encoding="utf-8").read()
assert "with sem" in src, "要用信号量限流"
assert peak <= 2, f"同时下载不应超过 2：{peak}"
