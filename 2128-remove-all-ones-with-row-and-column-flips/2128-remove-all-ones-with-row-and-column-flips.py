class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        def flipcolumn(columnidx):
            for rowidx, row in enumerate(grid):
                grid[rowidx][columnidx] = 1 - grid[rowidx][columnidx]
        
        def checkZeromatrix(grid):
            firstrow = grid[0]
            for idx, num in enumerate(firstrow):
                if num != 1:
                    flipcolumn(idx)

            # check each row
            for row in grid:
                if len(set(row)) != 1:
                    return False
            return True
        
        return checkZeromatrix(grid)