class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums = [val for val in nums]
        ans = heapq.nlargest(k, enumerate(nums), key = lambda val:val[1])
        ans.sort()
        return [val[1] for val in ans]
        
        
        
                