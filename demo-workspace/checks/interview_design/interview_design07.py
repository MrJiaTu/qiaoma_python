bf = BloomFilter()
bf.add("https://a.cn")
assert bf.might_contain("https://a.cn") is True
assert bf.might_contain("https://b.cn") is False, "没加过的应判断不存在（简版无冲突时）"
