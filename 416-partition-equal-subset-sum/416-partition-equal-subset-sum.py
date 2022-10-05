class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False
        
        target = total // 2
        @cache
        def dfs(idx, target):
            if target == 0:
                return True
            if target < 0 or idx >= len(nums):
                return False
            
            return dfs(idx + 1, target - nums[idx]) or dfs(idx + 1, target)
            
        return dfs(0, target)