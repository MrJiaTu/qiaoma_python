import copy

a = [["购物车", 1], ["购物车", 2]]
b = copy.deepcopy(a)
b[0].append("已修改")
affected = a[0][-1] == "已修改"
