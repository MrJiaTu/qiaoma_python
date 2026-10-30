def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

r1 = add_item("苹果")
r2 = add_item("香蕉")
