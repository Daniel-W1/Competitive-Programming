class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        ibound = lambda i : i >= 0 and i < len(grid)
        jbound = lambda j : j >= 0 and j < len(grid[0])
        visited = set()
        def dfs(sr, sc,visited):
            if not ibound(sr) or not jbound(sc) or grid[sr][sc] == "X" or (sr,sc) in visited:
                return 

            visited.add((sr,sc))    
            dfs(sr+1, sc,visited)
            dfs(sr, sc + 1,visited)
            dfs(sr - 1, sc,visited)
            dfs(sr, sc - 1,visited)
            
        for col in range(len(grid[0])):
            if grid[0][col] == "O":
                dfs(0,col,visited)
            if grid[len(grid)-1][col] == "O":
                dfs(len(grid)-1,col,visited)
                
        for row in range(len(grid)):
            if grid[row][0] == "O":
                dfs(row, 0,visited)
            if grid[row][len(grid[0])-1] == "O":
                dfs(row, len(grid[0])-1,visited)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "O" and (i,j) not in visited:
                    grid[i][j] = "X"
        
            

        