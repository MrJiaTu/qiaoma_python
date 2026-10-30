from contextlib import closing

class OldSpider:
    def __init__(self):
        self.closed = False

    def close(self):
        self.closed = True

spider = OldSpider()
with closing(spider):
    pass
