def paginate(items, page, size):
    start = (page - 1) * size
    return items[start:start + size]

feed = ["a", "b", "c", "d", "e"]
page1 = paginate(feed, 1, 2)
