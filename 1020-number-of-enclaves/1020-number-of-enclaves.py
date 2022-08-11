class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        ibound = lambda i : i >= 0 and i < len(grid)
        jbound = lambda j : j >= 0 and j < len(grid[0])
        def dfs(sr, sc):
            if not ibound(sr) or not jbound(sc) or grid[sr][sc] == 0:
                return 

            grid[sr][sc] = 0            
            dfs(sr+1, sc)
            dfs(sr, sc + 1)
            dfs(sr - 1, sc)
            dfs(sr, sc - 1)
            
        for col in range(len(grid[0])):
            if grid[0][col] == 1:
                dfs(0,col)
            if grid[len(grid)-1][col] == 1:
                dfs(len(grid)-1,col)
        for row in range(len(grid)):
            if grid[row][0] == 1:
                dfs(row, 0)
            if grid[row][len(grid[0])-1] == 1:
                dfs(row, len(grid[0])-1)
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    answer += 1
                    
        return answer
            