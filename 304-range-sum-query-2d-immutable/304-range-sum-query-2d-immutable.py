class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                up =  matrix[row-1][col] if row-1 >= 0 else 0
                left = matrix[row][col-1] if col-1 >= 0 else 0
                diagonal = matrix[row-1][col-1] if row-1 >= 0 and col-1>= 0 else 0
                
                matrix[row][col] += up + left - diagonal
        self.grid = matrix
        # print(self.grid)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.grid[row2][col2]
        sub1 = self.grid[row2][col1-1] if col1-1 >= 0 else 0
        sub2 = self.grid[row1-1][col2] if row1-1 >= 0 else 0
        
        diagonal = self.grid[row1-1][col1-1] if row1-1 >= 0 and col1-1 >= 0 else 0
        
        return total - sub1 - sub2 + diagonal


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
    '''
    
    time comp O(q*n^2)
    space comp O(1)
    
    
    precompute the sum of the numbers in each row,
    3, 3, 4, 8, |10
    5, 11, 14, 15,| 16
    1, 3, 3, 4,| 9
    
    time comp O(q * n)
    space comp O(1)
    
    time(n^2 + q)
    space O(1)
    '''