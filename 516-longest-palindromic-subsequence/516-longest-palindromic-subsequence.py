class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        dp = [[0 for char in s]  for char in s]
        for i in range(len(dp)):
            dp[i][i] = 1

        for start in range(1,len(dp)):
            right = start
            for left in range(len(dp)-start):
                if s[left] == s[right]:
                    dp[left][right] = 2+dp[left+1][right-1]
                else:
                    dp[left][right] = max(dp[left][right-1],dp[left+1][right])
                right += 1
        return dp[0][-1]
        
                    
                    
                
                