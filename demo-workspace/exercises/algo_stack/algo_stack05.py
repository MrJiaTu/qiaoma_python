# ============================================================
# 栈、队列与哈希表 05 · 字母异位词分组
# ============================================================
# 【题目】把异位词归到一组：["eat","tea","tan","ate","nat","bat"] → [[eat,tea,ate],[tan,nat],[bat]]。
# 【要求】实现 group_anagrams，用排序结果当哈希键。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
def group_anagrams(words):
    groups = {}
    for w in words:
        key = w  # 键没有归一化
        groups.setdefault(key, []).append(w)
    return sorted(sorted(g) for g in groups.values())
