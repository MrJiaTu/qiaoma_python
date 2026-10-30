def limit(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        if count > 2:
            return "系统繁忙"
        return func()
    return wrapper

@limit
def grab():
    return "已提交"

r1 = grab()
r2 = grab()
r3 = grab()
