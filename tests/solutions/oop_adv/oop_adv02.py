class Payment:
    def pay(self, amount):
        raise NotImplementedError

class Alipay(Payment):
    def pay(self, amount):
        return f"支付宝支付 {amount} 元"

receipt = Alipay().pay(25.0)
