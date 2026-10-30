def permute(nums):
    result = []

    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(list(path))
            return
        for i, x in enumerate(nums):
            if i in used:
                continue
            used.add(i)
            path.append(x)
            backtrack(path, used)
            path.pop()
            used.remove(i)

    backtrack([], set())
    return result
