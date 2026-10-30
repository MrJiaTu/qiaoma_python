src = open("exercises/concurrency/concurrency09.py", encoding="utf-8").read()
assert "pool.map" in src, "要用线程池的 map 执行"
assert results == ["图1", "图2", "图3", "图4", "图5"]
