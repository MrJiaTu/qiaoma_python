assert has_cycle(h) is True, "1→2→3→2 有环"
assert has_cycle(build([1, 2])) is False
assert has_cycle(build([])) is False
