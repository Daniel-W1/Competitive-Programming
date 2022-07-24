class Solution:
    def arrangeCoins(self, n: int) -> int:
        # [1, 2, 3]
        return int((math.sqrt(8 * n + 1)-1)/2)
            