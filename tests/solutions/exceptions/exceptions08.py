def validate(phone):
    if len(phone) != 11:
        raise ValueError("手机号必须是 11 位")

error = None
try:
    validate("13800")
except ValueError as e:
    error = str(e)
