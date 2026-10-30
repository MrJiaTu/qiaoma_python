import inspect
assert result == ["a\n", "b\n", "c\n"], f"内容要逐行：{result}"
assert not isinstance(read_lines("log.txt"), list), "应返回生成器而非列表"
