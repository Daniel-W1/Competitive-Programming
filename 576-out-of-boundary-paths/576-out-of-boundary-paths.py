class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, sr: int, sc: int) -> int:
        outboundx = lambda val : val > m-1 or val < 0
        outboundy = lambda val: val > n-1 or val < 0
        memo = {}
        def dfs(sr, sc, movecnt):
            if (sr,sc, movecnt) in memo: return memo[sr,sc,movecnt]
            if movecnt > maxMove:
                memo[sr,sc,movecnt] = 0
                return 0
            
            if outboundx(sr) or outboundy(sc):
                memo[sr,sc,movecnt] = 1
                return 1
           
            memo[sr,sc,movecnt] = dfs(sr+1, sc, movecnt+1) + dfs(sr-1, sc, movecnt+1) + dfs(sr, sc+1,movecnt+1) + dfs(sr, sc-1,movecnt+1)
            return memo[sr,sc,movecnt]
            
        
        return dfs(sr,sc,0) % (10**9+7)
        
        
                
            