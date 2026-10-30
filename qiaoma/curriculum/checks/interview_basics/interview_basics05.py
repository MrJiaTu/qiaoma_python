assert answer == "不会报错", "元组里嵌套的可变对象可以被修改"
assert t[1] == [2, 3, 4] and modified is False
