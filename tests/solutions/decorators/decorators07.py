import functools

def deco(func):
    @functools.wraps(func)
    def wrapper():
        return func()
    return wrapper

@deco
def pay():
    return "已支付"

name = pay.__name__
