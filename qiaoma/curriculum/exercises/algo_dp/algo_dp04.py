# ============================================================
# 递归回溯与入门DP 04 · 零钱兑换
# ============================================================
# 【题目】硬币 [1,2,5] 凑出 11 元最少要几枚：11 → 3（5+5+1）。凑不出返回 -1。
# 【要求】实现 coin_change(coins, amount)。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = dp[i - coin]  # 没 +1 也没取 min
    return dp[amount] if dp[amount] != float("inf") else -1
