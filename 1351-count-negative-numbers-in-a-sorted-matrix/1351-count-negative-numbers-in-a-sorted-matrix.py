class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for ind in range(len(grid)):
            left, right = 0, len(grid[0])-1
            while left <= right:
                mid = (left + right)//2
                if grid[ind][mid] >= 0:
                    left = mid + 1
                else:
                    right = mid - 1
            count += (len(grid[0]) - right-1)
        return count