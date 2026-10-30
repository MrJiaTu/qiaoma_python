class Shortener:
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self):
        self.counter = 0
        self.code_to_url = {}

    def encode(self, url):
        self.counter += 1
        n = self.counter
        code = ""
        while n:
            code = self.ALPHABET[n % 62] + code
            n //= 62
        self.code_to_url[code] = url
        return code

    def decode(self, code):
        return self.code_to_url.get(code)
