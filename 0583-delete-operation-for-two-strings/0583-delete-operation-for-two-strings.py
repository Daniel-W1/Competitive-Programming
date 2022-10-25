class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
    
        for idx1 in range(m-1, -1, -1):
            for idx2 in range(n-1, -1, -1):
                if word2[idx1] == word1[idx2]:
                    dp[idx1][idx2] = dp[idx1 + 1][idx2 + 1] + 1
                
                else:
                    dp[idx1][idx2] = max(dp[idx1 + 1][idx2], dp[idx1][idx2+1]) 
        
        return len(word1) + len(word2) - 2*dp[0][0]
    
    