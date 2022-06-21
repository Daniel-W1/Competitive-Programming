class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def dfs(i,j,visited):
            if (i,j) in visited:
                return False
            if i < 0 or i > len(grid)-1:
                return False
            if j < 0 or j > len(grid[0])-1:
                return False
            if grid[i][j] == "0":
                return False
            visited.add((i,j))
            dfs(i-1,j,visited)
            dfs(i+1,j,visited)
            dfs(i,j-1,visited)
            dfs(i,j+1,visited)
            return True
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dfs(i,j,visited):
                    answer += 1
        return answer