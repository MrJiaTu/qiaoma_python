from dataclasses import dataclass

@dataclass
class Order:
    amount: float

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("金额不能为负")

caught = False
try:
    Order(-5)
except ValueError:
    caught = True
