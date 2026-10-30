def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("余额不足")
    return balance - amount

error = None
try:
    withdraw(100, 500)
except ValueError as e:
    error = str(e)
