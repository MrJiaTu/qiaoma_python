src = open("exercises/concurrency/concurrency01.py", encoding="utf-8").read()
assert "t.start()" in src, "线程创建后要 start 才会执行"
assert done == ["完成"], f"线程应执行一次任务：{done}"
