def make_coupon(threshold, off):
    def redeem(price):
        if price >= threshold:
            return price - off
        return price
    return redeem

coupon = make_coupon(100, 20)
p1 = coupon(120)
p2 = coupon(80)
