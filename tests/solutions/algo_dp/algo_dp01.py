def fib(n):
    cache = {}

    def dp(i):
        if i < 2:
            return i
        if i not in cache:
            cache[i] = dp(i - 1) + dp(i - 2)
        return cache[i]

    return dp(n)
