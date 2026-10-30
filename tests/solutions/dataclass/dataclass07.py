def shipping_fee(weight: float, base: float) -> float:
    return base + weight * 3

fee = shipping_fee(2.0, 8.0)
