class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid[0])-1
        n = len(grid)-1
        memo = {}
        def findunique(a, b):
            if (a,b) not in memo:
                if a == m and b == n and grid[b][a] != 1:
                    return 1
                if a > m or b > n:
                    return 0
                if grid[b][a] == 1:
                    return 0
                memo[a,b]= findunique(a+1,b) + findunique(a,b+1)
            return memo[a,b]
        return findunique(0,0)
                