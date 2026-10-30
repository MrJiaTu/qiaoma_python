class Payment:
    def pay(self, amount):
        raise NotImplementedError("子类必须实现 pay")

class CashPayment(Payment):
    pass

error = None
try:
    CashPayment().pay(10)
except NotImplementedError:
    error = "必须实现"
