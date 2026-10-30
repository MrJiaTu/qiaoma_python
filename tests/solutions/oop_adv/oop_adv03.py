class Alipay:
    def pay(self, amount):
        return f"支付宝支付 {amount} 元"

class WechatPay:
    def pay(self, amount):
        return f"微信支付 {amount} 元"

def checkout(method, amount):
    return method.pay(amount)

r1 = checkout(Alipay(), 10)
r2 = checkout(WechatPay(), 20)
