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
        
        dp = [[0 for _ in range(int(s2+1))] for _ in range(len(nums))]
        
        # print(s2)
        # base cases
        for row in range(len(nums)):
            dp[row][0] = 1
        
        if nums[0] <= s2:
            dp[0][nums[0]] += 1
        
        for row in range(1,len(nums)):
            for col in range(int(s2 + 1)):
                if nums[row] > col:
                    dp[row][col] = dp[row-1][col]
                else:
                    # print(row, col)
                    dp[row][col] = dp[row-1][col] + dp[row-1][col - nums[row]]
        
        # print(dp)

        return dp[-1][-1]