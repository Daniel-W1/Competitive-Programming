class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def dfs(idx):
            if idx > len(nums)-1:
                return 0
            
            choice1 = dfs(idx+2) + nums[idx]
            choice2 = dfs(idx + 1)
            
            return max(choice1, choice2)
        
        return dfs(0)