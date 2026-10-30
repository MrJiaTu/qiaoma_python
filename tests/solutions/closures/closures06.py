from functools import reduce

cart = [29, 15, 8]
total = reduce(lambda a, b: a + b, cart)
