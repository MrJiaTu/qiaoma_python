class MyQueue:
    def __init__(self):
        self.a = []
        self.b = []

    def push(self, x):
        self.a.append(x)

    def pop(self):
        if not self.b:
            while self.a:
                self.b.append(self.a.pop())
        return self.b.pop()
