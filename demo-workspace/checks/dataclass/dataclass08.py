assert menu == {"鱼香肉丝": 28.0, "麻婆豆腐": 18.0}
src = open("exercises/dataclass/dataclass08.py", encoding="utf-8").read()
assert "Dict[str, float]" in src or "dict[str, float]" in src, "要给 menu 写 Dict[str, float] 类型注解"
