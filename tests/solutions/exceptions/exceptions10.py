status = None
try:
    order_id = 20260820
except ValueError:
    status = "失败"
else:
    status = "成功"
