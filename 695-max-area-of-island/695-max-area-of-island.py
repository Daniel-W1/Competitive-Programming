class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        answer = 0
        ibound = lambda i : i >= 0 and i < len(grid)
        jbound = lambda j : j >= 0 and j < len(grid[0])
        def dfs(sr, sc, visited):
            nonlocal cnt
            if not ibound(sr) or not jbound(sc) or (sr,sc) in visited:
                return 
            if grid[sr][sc] == 0:
                return
            cnt += 1
            visited.add((sr, sc))
            dfs(sr+1, sc, visited)
            dfs(sr, sc + 1, visited)
            dfs(sr - 1, sc, visited)
            dfs(sr, sc - 1, visited)
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == 1:
                    cnt = 0 
                    dfs(i,j, visited)
                    answer = max(answer, cnt)
        return answer
            
            