# ============================================================
# 大厂高频手撕题 03 · 最长公共前缀
# ============================================================
# 【题目】["flower","flow","flight"] → "fl"。
# 【要求】实现 longest_common_prefix(strs)。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix  # 没有缩短
    return prefix
