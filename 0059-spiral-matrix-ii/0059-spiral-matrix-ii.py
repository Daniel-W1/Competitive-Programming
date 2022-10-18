class Solution:
    def inbound(self, row, col, grid):
        m = len(grid)
        n = len(grid[0])
        
        return 0 <= row < m and 0 <= col < n
    
    def fill(self,direction):
        row, col = self.row, self.col 
        
        while self.inbound(row, col, self.grid) and self.grid[row][col] == 0:
            self.grid[row][col] = self.curnum
            row += direction[0]
            col += direction[1]
            self.curnum += 1
            self.filledcnt += 1
            # print(self.grid)
        
        self.row = row - direction[0]
        self.col = col - direction[1]
        
    def generateMatrix(self, n: int) -> List[List[int]]:
        '''
        1, 2, 3, 4, 5
                    6
                    7
                    8
        13   12   11  10
        '''
        self.filledcnt = 0
        self.grid = [[0 for col in range(n)] for row in range(n)]
        directions = [(0, 1),(1, 0), (0, -1), (-1, 0)]
        current_direction = 0
        self.row = 0
        self.col = 0
        self.curnum = 1
        
        while self.filledcnt < n**2:
            direction = directions[current_direction]
            self.fill(direction)
            current_direction += 1
            current_direction %= len(directions)
            direction = directions[current_direction]
            self.row += direction[0]
            self.col += direction[1]
        
        return self.grid
            
            
            
            
            
        