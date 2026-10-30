class Payment:
    def fee(self, amount):
        return amount * 0.006

class CreditCard(Payment):
    def fee(self, amount):
        return super().fee(amount) + amount * 0.002

fee = CreditCard().fee(1000)
