class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0]*len(s)
        
        for idx in range(len(s)):
            if s[idx] == ")":
                if idx - 1 >= 0 and s[idx-1] =="(":
                    left = dp[idx - 2] if idx - 2 >= 0 else 0
                    dp[idx] = left + 2
                
                elif dp[idx-1] != 0 and idx - dp[idx-1] - 1 >= 0:
                    if s[idx - dp[idx-1]-1] == "(":
                        left = dp[idx - dp[idx-1]-2] if idx - dp[idx-1] - 2>=0 else 0                          
                        dp[idx] = left + dp[idx-1] + 2
        return max(dp) if dp else 0
                    