assert edit_distance("马", "妈") == 1
assert edit_distance("kitten", "sitting") == 3
assert edit_distance("", "abc") == 3
assert edit_distance("same", "same") == 0
