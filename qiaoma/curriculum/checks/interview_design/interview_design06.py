sf = Snowflake(1)
ids = [sf.next_id(100) for _ in range(5)]
assert len(set(ids)) == 5, "同一毫秒必须生成不同 ID"
ids2 = [sf.next_id(101) for _ in range(3)]
assert len(set(ids + ids2)) == 8
