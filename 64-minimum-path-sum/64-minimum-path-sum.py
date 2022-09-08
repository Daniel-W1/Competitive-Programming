class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rowSize = len(grid)
        colSize = len(grid[0])
        
        @cache
        def dfs(row, col):
            if not 0 <= row < rowSize or not 0 <= col < colSize:
                return float('inf')
            
            if row == rowSize-1 and col == colSize-1:
                return grid[row][col]
            
            choice1 = dfs(row+1, col) + grid[row][col]
            choice2 = dfs(row, col+1) + grid[row][col]
            
            return min(choice1, choice2)
    
        return dfs(0,0)