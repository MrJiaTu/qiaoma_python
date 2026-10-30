assert fee == 14, f"2 公斤运费是 14，而不是 {fee}"
assert shipping_fee(0) == 8, "0 公斤应收首重 8 元"
