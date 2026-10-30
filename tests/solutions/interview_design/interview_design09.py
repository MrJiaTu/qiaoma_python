class Leaderboard:
    def __init__(self):
        self.scores = {}

    def update(self, player, score):
        self.scores[player] = score

    def top_k(self, k):
        ranking = sorted(self.scores, key=lambda p: (-self.scores[p], p))
        return ranking[:k]
