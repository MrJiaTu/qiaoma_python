import inspect
assert inspect.isgenerator(installments(6000, 3)), "要用 yield 写生成器"
assert list(installments(6000, 3)) == [2000.0, 2000.0, 2000.0]
