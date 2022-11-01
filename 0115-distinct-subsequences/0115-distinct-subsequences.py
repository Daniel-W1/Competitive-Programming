class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
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
            
            
            
            