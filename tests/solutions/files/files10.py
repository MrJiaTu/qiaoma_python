import json

wallet = {"balance": 88.5}
with open("wallet.json", "w", encoding="utf-8") as f:
    json.dump(wallet, f)
with open("wallet.json", encoding="utf-8") as f:
    loaded = json.load(f)
balance = loaded["balance"]
