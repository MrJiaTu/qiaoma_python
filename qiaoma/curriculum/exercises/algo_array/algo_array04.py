# ============================================================
# 数组与字符串双指针 04 · 三数之和
# ============================================================
# 【题目】找出所有和为 0 且不重复的三元组。例：[-1,0,1,2,-1,-4] → [[-1,-1,2],[-1,0,1]]。
# 【要求】实现 three_sum(nums)：排序 + 固定一个数 + 双指针。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
def three_sum(nums):
    result = []
    nums.sort()
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result  # 没有去重
