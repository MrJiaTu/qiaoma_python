steps = []

def auth(func):
    def wrapper():
        steps.append("auth")
        return func()
    return wrapper

def log(func):
    def wrapper():
        steps.append("log")
        return func()
    return wrapper

@auth
@log
def order():
    steps.append("order")

order()
