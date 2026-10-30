from dataclasses import dataclass, asdict

@dataclass
class Order:
    dish: str
    price: float

order = Order("酸辣粉", 12.0)
payload = asdict(order)
