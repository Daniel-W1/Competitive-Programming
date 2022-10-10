class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(1, 0),(0,1),(-1, 0),(0,-1)]
        m, n = len(grid), len(grid[0])
        
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    for dx, dy in directions:
                        newr, newc = r + dx , c + dy
                        if not 0 <= newr < m or not 0 <= newc < n:
                            ans += 1
                        
                        elif grid[newr][newc] == 0:
                            ans += 1
        
        return ans
                            