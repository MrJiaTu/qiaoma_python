class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def __gt__(self, other):
        return self.balance > other.balance

rich = Wallet(100) > Wallet(50)
