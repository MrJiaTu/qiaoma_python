# ============================================================
# 排序与二分 04 · 基础二分查找
# ============================================================
# 【题目】有序数组找目标值下标，找不到返回 -1。
# 【要求】实现 binary_search(nums, target)。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:  # 会漏掉最后一个元素
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
