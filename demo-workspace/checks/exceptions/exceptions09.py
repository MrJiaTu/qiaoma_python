assert success is True, "第三次请求成功，不应提前放弃"
assert attempts == 3, f"共尝试 3 次：{attempts}"
