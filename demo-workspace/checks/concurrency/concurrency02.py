src = open("exercises/concurrency/concurrency02.py", encoding="utf-8").read()
assert "t.join()" in src, "要 join 等待所有线程完成"
assert count == 3, f"等线程全部结束后应有 3 页：{count}"
