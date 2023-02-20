class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        
        prev_max = nums[-1]
        n = len(nums)
        ans = 0
        
        for idx in range(n-2, -1, -1):
            
            ans = max(ans, prev_max - nums[idx])
            prev_max = max(prev_max, nums[idx])
        
        return ans if ans else -1