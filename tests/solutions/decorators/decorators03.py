def double(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapper

@double
def price(n):
    return n

result = price(10)
