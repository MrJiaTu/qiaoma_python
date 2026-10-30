import inspect
gen = page_numbers(5)
assert inspect.isgenerator(gen), "应该返回生成器对象"
assert list(gen) == [1, 2, 3, 4, 5]
