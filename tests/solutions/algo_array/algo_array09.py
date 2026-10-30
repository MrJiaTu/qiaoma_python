def add_strings(a, b):
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result = []
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i])
        if j >= 0:
            total += int(b[j])
        result.append(str(total % 10))
        carry = total // 10
        i -= 1
        j -= 1
    return "".join(reversed(result))
