merged = merge_two(build([1, 3, 5]), build([2, 4, 6]))
assert to_list(merged) == [1, 2, 3, 4, 5, 6]
assert to_list(merge_two(build([]), build([1]))) == [1]
