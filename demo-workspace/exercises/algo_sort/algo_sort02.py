# ============================================================
# 排序与二分 02 · 手写快速排序
# ============================================================
# 【题目】分治：选基准，小的放左边大的放右边，递归。
# 【要求】实现 quick_sort(nums)。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left = [x for x in nums[1:] if x < pivot]
    right = [x for x in nums[1:] if x > pivot]  # 等于基准的丢了
    return quick_sort(left) + [pivot] + quick_sort(right)
