assert shipping_fee.__annotations__ == {"weight": float, "base": float, "return": float}, f"注解不完整：{shipping_fee.__annotations__}"
assert fee == 14.0
