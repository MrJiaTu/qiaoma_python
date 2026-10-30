class MinStack:
    def __init__(self):
        self.data = []
        self.mins = []

    def push(self, x):
        self.data.append(x)
        if not self.mins or x <= self.mins[-1]:
            self.mins.append(x)

    def pop(self):
        x = self.data.pop()
        if self.mins and x == self.mins[-1]:
            self.mins.pop()
        return x

    def get_min(self):
        return self.mins[-1]

s = MinStack()
for v in [3, 1, 2]:
    s.push(v)
m1 = s.get_min()
s.pop()
s.pop()
m2 = s.get_min()
