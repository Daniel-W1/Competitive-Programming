class Solution:
    def countPaths(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0,1)]
        mod = 10**9 + 7
        
        @cache
        def dfs(row, col):
            res = 1
            for dx, dy in directions:
                newr, newc = row + dx, col + dy
                if 0 <= newr < m and 0 <= newc < n:
                    if matrix[newr][newc] > matrix[row][col]:
                        res += dfs(newr, newc)
            return res
        
        ans = 0
        
        for r in range(m):
            for c in range(n):
                ans = (ans + dfs(r, c)) % mod
        
        return ans