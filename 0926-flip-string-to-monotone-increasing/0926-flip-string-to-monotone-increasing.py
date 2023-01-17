class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        
        @cache
        def dp(idx, one_seen):
            
            if idx == n:
                return 0
            
            
            if s[idx] == "0":
                return dp(idx + 1, one_seen) + int(one_seen)
            
            elif not one_seen:
                return min(dp(idx + 1, True), dp(idx + 1, False) + 1)
            
            else:
                return dp(idx + 1, True)
            
        
        return dp(0, False)
        
                
                