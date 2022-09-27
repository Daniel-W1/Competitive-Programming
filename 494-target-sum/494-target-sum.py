class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        real_target = (sum(nums) - target)/2
        
        @cache
        def dfs(idx, cursum):
            if idx >= len(nums):
                return int(cursum == real_target)
            
            choice1 = dfs(idx + 1, cursum)
            choice2 = dfs(idx + 1, cursum  + nums[idx])
            
            return choice1 + choice2
        
        return dfs(0, 0)