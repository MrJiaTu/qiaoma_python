from collections import Counter

orders = ["麻辣烫", "黄焖鸡", "麻辣烫", "米线", "麻辣烫"]
top_dish = Counter(orders).most_common(1)[0][0]
