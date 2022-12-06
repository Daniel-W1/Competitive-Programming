class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        directions = [-1,0,1]
        n, m = len(grid), len(grid[0])
        
        @cache
        def dp(row, col1, col2):
            if row == n:
                return 0
            
            if col1 == -1 or col1 == m or col2 == -1 or col2 == m:
                return -float('inf')
            
            total_cherry = 0
            if col1 == col2:
                total_cherry = grid[row][col1]
            else:
                total_cherry = grid[row][col1] + grid[row][col2]
        
            res = 0
            for dy in directions:
                new_col1 = col1 + dy
                
                for d2y in directions:
                    new_col2 = col2 + d2y
                    
                    res = max(res, dp(row+1, new_col1, new_col2) + total_cherry)
            
            return res
        
        return dp(0, 0, m-1)
        
            