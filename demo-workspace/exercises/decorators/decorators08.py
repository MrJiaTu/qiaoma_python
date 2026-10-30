# ============================================================
# 装饰器 08 · 缓存昂贵查询
# ============================================================
# 【场景】查余票接口很慢，同样的日期要缓存结果。
# 【任务】实现 memo 装饰器：相同参数只算一次。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
query_count = 0

def memo(func):
    cache = {}
    def wrapper(key):
        return func(key)  # 没走缓存
    return wrapper

@memo
def tickets(date):
    global query_count
    query_count += 1
    return f"{date}:有票"

tickets("09-30")
tickets("09-30")
tickets("10-01")
