content = open("ledger.txt", encoding="utf-8").read()
assert content == "8月20日 午餐 25元", f"账目没写进文件：{content!r}"
