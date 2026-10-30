assert to_list(remove_nth(build([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
assert to_list(remove_nth(build([1]), 1)) == []
assert to_list(remove_nth(build([1, 2]), 1)) == [1]
