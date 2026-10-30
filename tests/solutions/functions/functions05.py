def place_order(dish, count=1, note="无"):
    return f"{dish}x{count} 备注:{note}"

order = place_order("黄焖鸡", note="微辣")
