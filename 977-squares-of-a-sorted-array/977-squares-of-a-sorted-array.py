class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new = []
        for val in nums:
            if val < 0:
                new.append(-1*val)
            else:
                new.append(val)
        return [val**2 for val in sorted(new)]