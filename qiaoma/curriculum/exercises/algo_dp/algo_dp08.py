# ============================================================
# 递归回溯与入门DP 08 · 组合总和
# ============================================================
# 【题目】candidates=[2,3,6,7], target=7，数字可重复用，找出所有和为 7 的组合 → [[2,2,3],[7]]。
# 【要求】实现 combination_sum(candidates, target)。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
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
            backtrack(i + 1, path, remain - c)  # 可重复用，start 不该加一
            path.pop()

    backtrack(0, [], target)
    return result
