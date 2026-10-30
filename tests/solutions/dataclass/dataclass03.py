from dataclasses import dataclass

@dataclass
class Order:
    dish: str
    price: float
    delivery_fee: float = 3.0

    def total(self):
        return self.price + self.delivery_fee

order = Order("米线", 15.0)
pay = order.total()
