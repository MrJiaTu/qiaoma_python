class BloomFilter:
    def __init__(self, size=64):
        self.bits = [False] * size
        self.size = size

    def _hashes(self, item):
        return [hash(item) % self.size, hash(item + "#") % self.size]

    def add(self, item):
        for i in self._hashes(item):
            self.bits[i] = True

    def might_contain(self, item):
        return all(self.bits[i] for i in self._hashes(item))
