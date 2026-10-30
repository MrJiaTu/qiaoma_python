from dataclasses import dataclass, field

@dataclass
class Order:
    dish: str
    coupons: list = field(default_factory=list)

order = Order("盖饭")
assert order.coupons == []
