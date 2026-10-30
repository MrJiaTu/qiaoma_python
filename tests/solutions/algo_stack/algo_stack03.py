def daily_temperatures(t):
    result = [0] * len(t)
    stack = []
    for i, temp in enumerate(t):
        while stack and t[stack[-1]] < temp:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
    return result
