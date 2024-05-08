class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = lambda idx : ["Gold Medal","Silver Medal","Bronze Medal"][idx] if idx < 3 else str(idx + 1)
        sorted_score = sorted(score, reverse = True)
        score_idx_map = {val:idx for idx, val in enumerate(sorted_score)}
        
        return [rank(score_idx_map[val]) for val in score]