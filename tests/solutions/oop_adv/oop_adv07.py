class Payment:
    channels = []

class Alipay(Payment):
    channels = Payment.channels + ["支付宝"]

class WechatPay(Payment):
    channels = Alipay.channels + ["微信"]

channels = WechatPay.channels
