from dataclasses import dataclass

@dataclass(frozen=True)
class Order:
    order_no: str
    amount: float

order = Order("DD001", 25.0)
blocked = False
try:
    order.order_no = "DD999"
except Exception:
    blocked = True
