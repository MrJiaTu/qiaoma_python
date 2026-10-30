# ============================================================
# 递归回溯与入门DP 09 · N 皇后计数
# ============================================================
# 【题目】n=4 的棋盘放 4 个互不攻击的皇后，共 2 种方案。
# 【要求】实现 solve_n_queens(n) 返回方案数。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
def solve_n_queens(n):
    count = 0
    cols = set()
    diag1 = set()  # 主对角线：row - col
    diag2 = set()  # 副对角线：row + col

    def backtrack(row):
        nonlocal count
        if row == n:
            count += 1
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            backtrack(row + 1)
            # 忘了回溯撤销

    backtrack(0)
    return count
