assert menu.get("宫保鸡丁") == 32, f"新菜没上架：{menu}"
assert len(menu) == 3, f"菜单应该共 3 道菜：{menu}"
