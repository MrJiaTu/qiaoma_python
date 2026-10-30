assert page1 == ["a", "b"], f"第 1 页应是前两条：{page1}"
assert paginate(feed, 2, 2) == ["c", "d"]
