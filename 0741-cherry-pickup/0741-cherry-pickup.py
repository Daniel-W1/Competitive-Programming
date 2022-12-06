class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1, 0), (0, 1)]
        
        @cache
        def dfs(row1, col1, row2, col2):
            if row1 == n or row2 == n or col1 == n or col2 == n:
                return -float('inf')
            
            if grid[row1][col1] == -1 or grid[row2][col2] == -1:
                return -float('inf')
            
            if row1 == col1 == n-1:
                return grid[n-1][n-1]
            
            # collect the cherries
            total_cherry = 0
            if row1 == row2 and col1 == col2:
                total_cherry += grid[row1][col1]
            
            else:
                total_cherry = grid[row1][col1] + grid[row2][col2]
            
            
            res = -float('inf')
            for dx, dy in directions:
                new_r1, new_c1 = row1 + dx, col1 + dy
                
                for d2x, d2y in directions:
                    new_r2, new_c2 = row2 + d2x, col2 + d2y
                    res = max(res, dfs(new_r1, new_c1, new_r2, new_c2) + total_cherry)
            
            return res

        
        ans =  dfs(0, 0, 0, 0) 
        return ans if ans != -float('inf') else 0