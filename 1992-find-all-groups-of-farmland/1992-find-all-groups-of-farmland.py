class Solution:
    def findFarmland(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    
                    for row in range(r, len(grid)+1):
                        if not row < len(grid) or not grid[row][c]: break
                        
                        for col in range(c, len(grid[0])+1):
                            if not col < len(grid[0]) or not grid[row][col]: break
                            grid[row][col] = 0
                
                    ans.append([r, c, row-1, col-1])
            
        return ans