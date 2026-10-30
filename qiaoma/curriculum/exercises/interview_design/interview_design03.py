# ============================================================
# 场景设计题 03 · 短链服务
# ============================================================
# 【场景】自增 ID 转 62 进制生成短码，并支持短码反查长链。
# 【要求】实现 Shortener 的 encode/decode。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
class Shortener:
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self):
        self.counter = 0
        self.code_to_url = {}

    def encode(self, url):
        self.counter += 1
        code = str(self.counter)  # 没转 62 进制
        self.code_to_url[code] = url
        return code

    def decode(self, code):
        return self.code_to_url.get(code)
