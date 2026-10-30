def combination_sum(candidates, target):
    result = []

    def backtrack(start, path, remain):
        if remain == 0:
            result.append(list(path))
            return
        for i in range(start, len(candidates)):
            c = candidates[i]
            if c > remain:
                continue
            path.append(c)
            backtrack(i, path, remain - c)
            path.pop()

    backtrack(0, [], target)
    return result
