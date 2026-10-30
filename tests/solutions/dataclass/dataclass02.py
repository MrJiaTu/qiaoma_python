from dataclasses import dataclass

@dataclass
class Order:
    dish: str
    delivery_fee: float = 3.0
    paid: bool = False

order = Order("麻辣烫")
