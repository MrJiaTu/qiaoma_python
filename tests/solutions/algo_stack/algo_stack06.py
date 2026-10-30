from collections import Counter

def top_k(nums, k):
    counts = Counter(nums)
    return [x for x, _ in counts.most_common(k)]
