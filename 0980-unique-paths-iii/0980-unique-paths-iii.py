class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        # cnt non obstacle cells
        obs = sum([row.count(-1) for row in grid])
        n, m = len(grid), len(grid[0])
        
        non_obs = n*m - obs - 1
        visited = set()
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def dfs(r, c, cnt):
            
            if grid[r][c] == -1:
                return 0
            
            if grid[r][c]== 2:
                return cnt == non_obs
            
            res = 0
            visited.add((r, c))
            for dx, dy in directions:
                newr, newc = r + dx, c + dy
                
                if 0 <= newr< n and 0 <= newc < m:
                    if (newr, newc) not in visited:
                        res += dfs(newr, newc, cnt + 1)
            
            visited.remove((r, c))
            
            return res
        
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    return dfs(r, c, 0)
                
            
            