head = build([1, 2, 3, 4, 5])
assert to_list(reverse_list(head)) == [5, 4, 3, 2, 1]
assert to_list(reverse_list(build([]))) == []
assert to_list(reverse_list(build([1]))) == [1]
