# ============================================================
# 文件读写 10 · JSON 存余额
# ============================================================
# 【场景】钱包余额要持久化成 JSON，下次启动读回来。
# 【任务】修复代码，用 json 模块写入并读回。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
import json

wallet = {"balance": 88.5}
with open("wallet.json", "w", encoding="utf-8") as f:
    f.write(str(wallet))  # str 不是合法 JSON
with open("wallet.json", encoding="utf-8") as f:
    loaded = json.load(f)
balance = loaded["balance"]
