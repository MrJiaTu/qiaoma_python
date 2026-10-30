# ============================================================
# 排序与二分 08 · 二分求平方根
# ============================================================
# 【题目】不用 math.sqrt，整数部分向下取整：my_sqrt(8) → 2。
# 【要求】实现 my_sqrt(x)。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
def my_sqrt(x):
    if x < 2:
        return x
    left, right = 1, x
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        if mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return left  # 退出时 right 才是答案
