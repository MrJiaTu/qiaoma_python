assert affected is False, "深拷贝后改 b 不应影响 a"
import copy as _c
assert b[0] == ["购物车", 1, "已修改"] and a[0] == ["购物车", 1]
