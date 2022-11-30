class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(dict)
        
        # print(dp)
        answer = 0
        
        for idx, num in enumerate(nums):
            for idx2 in range(idx-1, -1, -1):
                
                diff = nums[idx] - nums[idx2]
                # first initialise it
                if diff not in dp[idx]:
                    dp[idx][diff] = 1 
                
                if diff not in dp[idx2]:
                    dp[idx2][diff] = 1
                    
                dp[idx][diff] = max(dp[idx][diff], dp[idx2][diff] + 1)
                answer = max(answer, dp[idx][diff])
                
        return answer