class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        this is counting dp and here is how we are going to do it
        
        s1 - s2 = target 
        s1 = total - s2
        total - s2 - s2 = target
        total - target = 2*s2
        s2 = (total - target)/2
        
        
        '''
        total = sum(nums)
        s2 = (total - target)/2
    
        
        if int(s2) != s2 or s2 < 0: return 0
        
        dp = [0 for _ in range(int(s2+1))] 
        cur = [0 for _ in range(int(s2+1))]
        
        # print(s2)
        # base cases
        for row in range(len(nums)):
            dp[0] = 1
            cur[0] = 1
        
        if nums[0] <= s2:
            dp[nums[0]] += 1
        
        for row in range(1,len(nums)):
            for col in range(int(s2 + 1)):
                if nums[row] > col:
                    cur[col] = dp[col]
                else:
                    # print(row, col)
                    cur[col] = dp[col] + dp[col - nums[row]]
            dp, cur = cur, dp
        
        # print(dp)
        return dp[-1]
    
        '''
        okay cool can u optimise the space ?

        '''