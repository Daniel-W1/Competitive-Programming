class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        '''
        so how are we going to solve this problem
        
        so one observation would be if our o is connected to the edge
        it won't be counted right in any way
        
        
        so one approach would be to go over the edges and make dfs calls when ever we find a 0 node
        
        after that it would be a normal dfs problem
        '''
        n, m = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(row, col):
            grid[row][col] = 1
            for dx, dy in directions:
                newr, newc = row + dx, col + dy
                if 0 <= newr < n and 0 <= newc < m and grid[newr][newc] == 0:
                    dfs(newr, newc)
        
        
       
        # instead of using an invalid set we can make the 0s one and
        # go
        for col in range(m):
            if grid[0][col] == 0:
                # print("here", col)
                dfs(0, col)
            if grid[n-1][col] == 0:
                dfs(n-1, col)
            
        # go through the left and the right
        for row in range(n):
            if grid[row][0] == 0:
                dfs(row, 0)
            if grid[row][m-1] == 0:
                dfs(row, m-1)
        
        ans = 0
        # print(grid)
        for row in range(1, n-1):
            for col in range(1, m-1):
                if grid[row][col] == 0:
                    dfs(row, col)
                    ans += 1
        
        
        return ans
            
        # time and space comp O(n*m) space comp O(1)