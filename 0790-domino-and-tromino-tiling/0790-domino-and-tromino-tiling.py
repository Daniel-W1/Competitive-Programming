class Solution:
    def numTilings(self, n: int) -> int:
        m = 10**9 + 7
        dp = [[0 for _ in range(2)] for _ in range(n+2)]
        dp[n][0] = 1
        
        for size in range(n-1, -1, -1):
            for state in range(2):
                if not state:
                    dp[size][state] = (dp[size+1][state] + dp[size +2][state] + 2*dp[size + 1][1])%m
                else:
                    dp[size][state] = (dp[size + 1][1] + dp[size + 2][0])%m
        
        # print(dp)
        return dp[0][0]