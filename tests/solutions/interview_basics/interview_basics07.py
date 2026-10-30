def big_sum(n):
    return sum(x * 2 for x in range(n))

answer = "省内存"
total = big_sum(1000)
