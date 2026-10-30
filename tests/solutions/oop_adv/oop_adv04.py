class UnionPay:
    def __init__(self, card_no):
        self.card_no = card_no

    def __str__(self):
        return f"**** **** **** {self.card_no[-4:]}"

card = UnionPay("6222020200111234")
display = str(card)
