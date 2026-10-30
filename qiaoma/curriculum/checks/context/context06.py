assert hasattr(t, "elapsed") and t.elapsed >= 0.05, f"要记录耗时：{getattr(t, 'elapsed', None)}"
