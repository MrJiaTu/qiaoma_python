def age_sort(ages):
    counts = [0] * 131
    for age in ages:
        counts[age] += 1
    result = []
    for age, c in enumerate(counts):
        result.extend([age] * c)
    return result
