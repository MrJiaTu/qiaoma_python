calls = []

def log(func):
    def wrapper():
        calls.append("开始处理")
        func()
    return wrapper

@log
def place_order():
    calls.append("下单")

place_order()
