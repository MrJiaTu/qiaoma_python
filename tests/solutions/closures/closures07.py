def pipe(funcs):
    def run(price):
        for f in funcs:
            price = f(price)
        return price
    return run

promo = pipe([lambda p: p * 0.8, lambda p: p - 20])
final = promo(200)
