password = "abc12345"
if len(password) >= 8 and any(ch.isdigit() for ch in password):
    strength = "强"
else:
    strength = "弱"
