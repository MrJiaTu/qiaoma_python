# ============================================================
# 场景设计题 10 · 配置中心（观察者）
# ============================================================
# 【场景】配置变更要通知所有订阅的服务：实现发布-订阅。
# 【要求】实现 ConfigCenter 的 subscribe/set。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
class ConfigCenter:
    def __init__(self):
        self.config = {}
        self.listeners = []

    def subscribe(self, callback):
        self.listeners.append(callback)

    def set(self, key, value):
        self.config[key] = value
        # 忘了通知订阅者
