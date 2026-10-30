# ============================================================
# 场景设计题 09 · 排行榜 Top K
# ============================================================
# 【场景】游戏排行榜：实时维护分数最高的 k 名玩家。
# 【要求】实现 Leaderboard.top_k(k)，分数相同按名字字典序。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
class Leaderboard:
    def __init__(self):
        self.scores = {}

    def update(self, player, score):
        self.scores[player] = score

    def top_k(self, k):
        return list(self.scores)[:k]  # 没按分数排序
