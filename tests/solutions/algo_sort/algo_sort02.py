def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left = [x for x in nums[1:] if x < pivot]
    mid = [x for x in nums if x == pivot]
    right = [x for x in nums[1:] if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)
