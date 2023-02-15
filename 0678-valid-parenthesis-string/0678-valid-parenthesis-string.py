class Solution:
    def checkValidString(self, s: str) -> bool:
        
        n = len(s)
        
        @cache
        def dp(idx, cur):
            
            if cur < 0:
                return False
            
            if idx == n:
                return cur == 0
            
            if s[idx] == "(":
                return dp(idx + 1, cur + 1)
            
            elif s[idx] == ")":
                return dp(idx+1, cur-1)
            
            return dp(idx+1, cur-1) or dp(idx+1, cur+1) or dp(idx+1, cur)
        
        # print(dp(0, 0))
        
        return dp(0, 0)