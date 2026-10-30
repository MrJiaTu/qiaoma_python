raw = ["¥3.5", "¥6.0", "¥12.5"]
prices = [float(r.replace("¥", "")) for r in raw]
