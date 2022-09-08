class Solution:
    def rob(self, nums: List[int]) -> int:
        
        '''
        @cache
        def dfs(idx):
            if idx > len(nums)-1:
                return 0
            
            choice1 = dfs(idx+2) + nums[idx]
            choice2 = dfs(idx + 1)
            
            return max(choice1, choice2)
        
        return dfs(0)
        
        '''
        '''
        dp = [0]*len(nums)
        dp[0] = nums[0]
        
        for idx in range(1, len(nums)):
            if idx > 1:
                dp[idx] = max(dp[idx-2]+nums[idx], dp[idx-1])
            else:
                dp[idx] = max(nums[idx], dp[idx-1])
                
        return dp[-1]
        '''
       # time O(n), space O(n), space can be optimised to O(1)
        prev1 = nums[0]
        prev2 = -1
        cur = nums[0]
        
        for idx in range(1, len(nums)):
            if idx > 1:
                cur = max(prev2 + nums[idx], prev1)
            else:
                cur = max(nums[idx], prev1)
            prev1, prev2 = cur, prev1
            
        return cur
        # time O(n), space O(1)