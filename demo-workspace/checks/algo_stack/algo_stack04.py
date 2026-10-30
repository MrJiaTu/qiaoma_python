q = MyQueue()
for v in [1, 2, 3]:
    q.push(v)
assert q.pop() == 1, "队列应先进先出"
assert q.pop() == 2
q.push(4)
assert q.pop() == 3
assert q.pop() == 4
