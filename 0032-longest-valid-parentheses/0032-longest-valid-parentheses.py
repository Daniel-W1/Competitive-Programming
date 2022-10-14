class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0]*len(s)
        for idx, char in enumerate(s):
            if char == ")":
                if idx >= 1 and s[idx-1] == "(":
                    left = dp[idx - 2] if idx - 2 >= 0 else 0
                    dp[idx] = left + 2
                elif idx >= 1 and s[idx-1] == ")":
                    if dp[idx-1] == 0:
                        dp[idx-1] = 0
                    else:
                        last = idx - dp[idx-1] - 1
                        if last >= 0 and s[last] == "(":
                            left = dp[last-1] if last - 1 >= 0 else 0
                            dp[idx] = dp[idx-1] + left + 2

        # print(dp)
        return max(dp) if dp else 0
                    
                    
            
            