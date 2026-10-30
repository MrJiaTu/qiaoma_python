class RedPacket:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return RedPacket(self.amount + other.amount)

merged = RedPacket(6.6) + RedPacket(8.8)
