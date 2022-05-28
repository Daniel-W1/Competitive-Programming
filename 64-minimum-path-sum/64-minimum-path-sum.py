class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid[0])-1
        n = len(grid)-1
        memo = {}
        def findminsum(a,b):
            if (a,b) not in memo:
                if a == m and b == n:
                    return grid[b][a]
                if a > m or b > n:
                    return float('inf')
                memo[a,b] = min(findminsum(a+1,b)+grid[b][a] , findminsum(a,b+1)+grid[b][a])
            return memo[a,b]
        return findminsum(0,0)