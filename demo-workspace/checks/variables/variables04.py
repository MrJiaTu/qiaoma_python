assert isinstance(height_m, float), "height_m 应该是小数（float）"
assert abs(height_m - 1.65) < 1e-9, f"165 厘米应该等于 1.65 米，而不是 {height_m}"
