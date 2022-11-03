class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        ROWS, COLS = len(grid), len(grid[0])

        for row in range(1, ROWS):
            curr_row = ''.join(str(val) for val in grid[row])
            prev_row = ''.join(str(val) for val in grid[row-1])
            xor = int(curr_row, 2) ^ int(prev_row, 2)
            # print(xor)
            if xor != 0 and xor != (2**COLS) - 1:
                return False
        return True