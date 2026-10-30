a = [1, 1, 2]
k = remove_duplicates(a)
assert k == 2 and a[:k] == [1, 2], f"去重后前 {k} 项应为 [1, 2]：{a}"
b = [0, 0, 1, 1, 1, 2, 2]
assert remove_duplicates(b) == 3 and b[:3] == [0, 1, 2]
