import random as _r
random.seed(7)
packets = split_red_packet(1000, 10)
assert len(packets) == 10
assert all(p >= 1 for p in packets), "每个红包至少 1 分"
assert sum(packets) == 1000, "总额必须守恒"
packets2 = split_red_packet(1, 1)
assert packets2 == [1]
