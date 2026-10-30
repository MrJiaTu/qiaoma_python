from dataclasses import field
order2 = Order("盖饭")
order.coupons.append("满减券")
assert order2.coupons == [], "不同订单不能共享同一个列表"
