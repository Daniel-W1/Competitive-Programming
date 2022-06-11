class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for val in nums:
            x ^= val
        return x