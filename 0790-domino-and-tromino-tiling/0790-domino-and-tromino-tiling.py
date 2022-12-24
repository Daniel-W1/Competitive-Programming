class Solution:
    def numTilings(self, n: int) -> int:
        m = 10**9 + 7
        dp = [[0 for _ in range(2)] for _ in range(n+1)]
        dp[n][0] = 1
        
        for size in range(n-1, -1, -1):
            for state in range(2):
                if not state:
                    choice1 = dp[size+1][state] if size + 1 <= n else 0
                    choice2 = dp[size +2][state] if size + 2 <= n else 0
                    choice3 = 2*dp[size + 1][1] if size + 1 <= n else 0
                    
                    dp[size][state] = (choice1 + choice2 + choice3)%m
                    
                else:
                    choice1 = dp[size + 1][1] if size + 1 <= n else 0
                    choice2 = dp[size + 2][0] if size + 2 <= n else 0
                    dp[size][state] = (choice1 + choice2)%m
        
        # print(dp)
        return dp[0][0]