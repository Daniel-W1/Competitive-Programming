class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False
        
        target = total // 2
        
        dp = [False for _ in range(target + 1)] 
        cur = [False for _ in range(target + 1)] 
        
        for idx in range(len(nums)):
            dp[0] = True
            cur[0] = True
        
        if nums[0] <= target: dp[nums[0]] = True
            
        for idx in range(1, len(nums)):
            for target in range(target + 1):
                
                if nums[idx] > target:
                    cur[target] = dp[target]
                
                else:
                    cur[target] = dp[target] or dp[target - nums[idx]]
            
            dp, cur = cur, dp
        return dp[-1]
    #  time and space O(n*target), n = len(nums)
    # time O(n*target), space O(n)
    
                