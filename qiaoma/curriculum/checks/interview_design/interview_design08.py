assert retry_delays(3, 5) == [1, 2, 4]
assert retry_delays(10, 3) == [1, 2, 4]
assert retry_delays(0, 3) == []
