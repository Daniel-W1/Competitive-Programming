class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(i,j,visited):
            if (i,j) in visited:
                return
            if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[0])-1:
                return
            if grid[i][j] == 0:
                return
            self.cnt += 1
            visited.add((i,j))
            dfs(i+1,j,visited)
            dfs(i-1,j,visited)
            dfs(i,j+1,visited)
            dfs(i,j-1,visited)
        
        ans = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if (i,j) not in visited:
                        self.cnt = 0
                        dfs(i,j,visited)
                        ans = max(ans,self.cnt)
        return ans