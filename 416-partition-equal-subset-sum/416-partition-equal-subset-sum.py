class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False
        
        target = total // 2
        
        dp = [[False for _ in range(target + 1)] for _ in range(len(nums))]
        
        for idx in range(len(nums)):
            dp[idx][0] = True
        
        if nums[0] <= target: dp[0][nums[0]] = True
            
        for idx in range(1, len(nums)):
            for target in range(target + 1):
                if nums[idx] > target:
                    dp[idx][target] = dp[idx-1][target]
                
                else:
                    dp[idx][target] = dp[idx-1][target] or dp[idx-1][target - nums[idx]]
        
        return dp[-1][-1]
                