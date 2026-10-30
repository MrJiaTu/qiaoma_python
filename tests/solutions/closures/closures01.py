def make_discount(rate):
    def discount(price):
        return price * rate
    return discount

eight = make_discount(0.8)
sale = eight(100)
