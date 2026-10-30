# ============================================================
# 面向对象进阶 03 · 多态收银台
# ============================================================
# 【场景】收银台 checkout 对任意支付方式调用 pay，体现多态。
# 【任务】修复 checkout，让它调用传入支付对象的 pay。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
class Alipay:
    def pay(self, amount):
        return f"支付宝支付 {amount} 元"

class WechatPay:
    def pay(self, amount):
        return f"微信支付 {amount} 元"

def checkout(method, amount):
    return "支付宝支付"  # 写死了，没用多态

r1 = checkout(Alipay(), 10)
r2 = checkout(WechatPay(), 20)
