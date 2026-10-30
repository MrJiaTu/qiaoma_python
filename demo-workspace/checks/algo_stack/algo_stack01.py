assert is_valid("()[]{}") is True
assert is_valid("(]") is False
assert is_valid("(") is False
assert is_valid("([{}])") is True
