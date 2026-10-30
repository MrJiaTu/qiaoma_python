from dataclasses import dataclass

@dataclass
class Order:
    dish: str
    price: float

order = Order("黄焖鸡", 25.0)
