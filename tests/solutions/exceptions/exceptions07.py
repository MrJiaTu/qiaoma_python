class InsufficientBalanceError(Exception):
    pass

def pay(balance, price):
    if price > balance:
        raise InsufficientBalanceError("余额不足")
    return balance - price

caught = None
try:
    pay(10, 25)
except InsufficientBalanceError:
    caught = "余额不足"
