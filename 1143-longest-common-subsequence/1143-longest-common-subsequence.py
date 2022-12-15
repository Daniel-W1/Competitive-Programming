class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [0 for _ in range(n+1)]
        cur_dp = [0 for _ in range(n+1)]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                
                if text1[j] == text2[i]:
                    cur_dp[j] = dp[j+1] + 1
                
                else:
                    cur_dp[j] = max(dp[j], cur_dp[j+1])
            # print(dp, cur_dp)
            cur_dp, dp = dp, cur_dp
        
        return dp[0]
        