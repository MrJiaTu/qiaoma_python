class Order:
    def __init__(self, order_no):
        self.order_no = order_no

    def __eq__(self, other):
        return isinstance(other, Order) and self.order_no == other.order_no

    def __hash__(self):
        return hash(self.order_no)

orders = {Order("A1"), Order("A1"), Order("B2")}
count = len(orders)
