class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def findpath(a,b):
            if (a,b) not in memo:
                if a == m and b == n:
                    return 1
                if a > m or b > n:
                    return 0
                memo[a,b]=  findpath(a+1, b) + findpath(a,b+1)
            return memo[a,b]
        return findpath(1,1)