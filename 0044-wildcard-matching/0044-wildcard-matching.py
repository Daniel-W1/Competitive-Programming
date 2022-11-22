class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache         
        def dfs(i, j):
            if i >= len(s) and j >= len(p):
                return True
            
            if j >= len(p):
                return False
            
            if i < len(s) and (s[i] == p[j] or p[j] == "?"):
                return dfs(i+1, j+1)
            
            elif p[j] == "*":
                return (i < len(s) and dfs(i+1, j)) or dfs(i, j+1) 
            
            return False
        
        return dfs(0, 0)