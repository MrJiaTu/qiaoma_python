query_count = 0

def memo(func):
    cache = {}
    def wrapper(key):
        if key not in cache:
            cache[key] = func(key)
        return cache[key]
    return wrapper

@memo
def tickets(date):
    global query_count
    query_count += 1
    return f"{date}:有票"

tickets("09-30")
tickets("09-30")
tickets("10-01")
