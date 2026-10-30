def has_pair_with_diff(nums, k):
    seen = set()
    for x in nums:
        if x - k in seen or x + k in seen:
            return True
        seen.add(x)
    return False
