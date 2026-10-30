goods = [("月饼", 300), ("大闸蟹", 500), ("茶叶", 200)]
ranking = sorted(goods, key=lambda g: g[1], reverse=True)
