class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        new = [0]*len(nums)
        
        for idx in range(len(nums)):
            for other in range(idx-1, -1, -1):
                if nums[idx] > nums[other]:
                    if dp[other]+1 > dp[idx]:
                        new[idx] = new[other]
                    elif dp[other]+1 == dp[idx]:
                        new[idx] += new[other]
                        
                    dp[idx] = max(dp[idx], dp[other]+1)
                    
            if new[idx] == 0:
                new[idx] = 1
        
        ans = 0
        the_max = max(dp)

        for idx in range(len(nums)):
            if dp[idx] == the_max:
                ans += new[idx]

        return ans
                
                        
                    
        
        