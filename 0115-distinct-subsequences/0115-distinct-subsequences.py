class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        n1, n2 = len(s), len(t)
        @cache
        def dfs(idx1, idx2):
            if idx2 == n2:
                return 1
            
            if idx1 == n1:
                return 0
            
            if s[idx1] == t[idx2]:
                return dfs(idx1 + 1, idx2 + 1) + dfs(idx1 + 1, idx2)
            
            return dfs(idx1 + 1, idx2)
        
        return dfs(0, 0)
        '''
        n1, n2 = len(s), len(t)
        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        
        for idx in range(n1+1):
            dp[idx][n2] = 1
        
        for idx in range(n2):
            dp[n1][idx] = 0
            
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]
        
        return dp[0][0]
    
        
        
        
        
        
        
        