class ConfigCenter:
    def __init__(self):
        self.config = {}
        self.listeners = []

    def subscribe(self, callback):
        self.listeners.append(callback)

    def set(self, key, value):
        self.config[key] = value
        for callback in self.listeners:
            callback(key, value)
