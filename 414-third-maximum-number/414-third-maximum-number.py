class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        return heapq.nlargest(3,list(set(nums)))[-1] if len(list(set(nums))) >= 3 else max(nums)