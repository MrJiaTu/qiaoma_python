from dataclasses import dataclass

@dataclass
class Order:
    dish: str
    price: float

a = Order("炒饭", 18)
b = Order("炒饭", 18)
same = a == b
