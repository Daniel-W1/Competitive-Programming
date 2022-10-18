class Solution:
    def inbound(self, row, col, grid):
        m = len(grid)
        n = len(grid[0])
        
        return 0 <= row < m and 0 <= col < n
    
    def fill(self,direction, row, col, grid, curnum):
        while self.inbound(row, col, grid) and grid[row][col] == 0:
            grid[row][col] = curnum
            row += direction[0]
            col += direction[1]
            curnum += 1
            self.filledcnt += 1
        
        row -= direction[0]
        col -= direction[1]
        
        return row, col, curnum
        
    def generateMatrix(self, n: int) -> List[List[int]]:
        self.filledcnt = 0
        grid = [[0 for col in range(n)] for row in range(n)]
        directions = [(0, 1),(1, 0), (0, -1), (-1, 0)]
        current_idx = 0
        row = 0
        col = 0
        current_num = 1
        
        while self.filledcnt < n**2:
            direction = directions[current_idx]
            row, col, current_num = self.fill(direction, row, col, grid, current_num)
            current_idx += 1
            current_idx %= len(directions)
            direction = directions[current_idx]
            row += direction[0]
            col += direction[1]
        
        return grid
            
            
            
            
            
        