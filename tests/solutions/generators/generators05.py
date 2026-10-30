orders = [500, 1200, 300, 2000, 800]
big = (o for o in orders if o > 1000)
result = list(big)
