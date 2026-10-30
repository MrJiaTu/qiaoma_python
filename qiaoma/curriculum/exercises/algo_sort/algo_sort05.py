# ============================================================
# 排序与二分 05 · 二分找左边界
# ============================================================
# 【题目】有序数组含重复值，找 target 第一次出现的下标：[1,2,2,2,3], 2 → 1。
# 【要求】实现 lower_bound(nums, target)。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
def lower_bound(nums, target):
    left, right = 0, len(nums) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:  # 找成上界了，等号丢了
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans
