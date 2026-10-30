def read_health_record(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "无记录"

record = read_health_record("不存在的档案.txt")
