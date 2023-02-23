class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        dp = defaultdict(lambda: 1)
        n = len(nums)
        ans = 0
        
        for idx in range(n):
            
            for idx2 in range(idx-1, -1, -1):
                
                diff = nums[idx] - nums[idx2]
                dp[idx, diff] = max(dp[idx, diff], dp[idx2, diff] + 1)
                ans = max(ans, dp[idx, diff])
        
        # print(dp)
        return ans
                