events = []
cc = ConfigCenter()
cc.subscribe(lambda k, v: events.append((k, v)))
cc.set("theme", "dark")
cc.set("lang", "zh")
assert events == [("theme", "dark"), ("lang", "zh")], f"订阅者要收到通知：{events}"
assert cc.config == {"theme": "dark", "lang": "zh"}
