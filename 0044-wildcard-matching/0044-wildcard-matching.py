class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        '''
        ? increament both pointers
        
        if both are characters increment both pointers
        
        if * do the majic trick
        
        '''
        if not s and p: return set(p) == {"*"}
        n1, n2 = len(s), len(p)
        
        @cache
        def dp(idx1, idx2):
    
            if idx1 == n1 and idx2 == n2:
                return True
            
            if idx1 == n1 and p[idx2] == "*":
                return dp(idx1, idx2+1)
            
            if idx2 == n2 or idx1 == n1: return False
            
            if s[idx1] == p[idx2]:
                return dp(idx1 + 1, idx2 + 1)
            
            elif p[idx2] == "?":
                return dp(idx1 + 1, idx2 + 1)
            
            elif p[idx2] == "*":
                return dp(idx1, idx2+1) or dp(idx1 + 1, idx2) or dp(idx1 + 1, idx2 + 1)
        
        return dp(0, 0)
                
        