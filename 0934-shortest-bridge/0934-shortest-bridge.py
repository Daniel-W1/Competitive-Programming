class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        the_map = {}
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        m, n = len(grid), len(grid[0])
        q = deque([])
        
        def dfs(row, col):
            grid[row][col] = 0
            q.append((row, col))
            
            for dx, dy in directions:
                newr, newc = row + dx, col + dy
                if (newr, newc) not in the_map and 0 <= newr < m and 0 <= newc < n:
                    if grid[newr][newc] == 1:
                        dfs(newr, newc)
        
        rep1 = None
        found = False
        for r in range(m):
            for c in range(n):
                if (r, c) not in the_map and grid[r][c] == 1:
                    dfs(r, c)
                    rep1 = (r, c)
                    found = True
                    break
            if found:
                break
        
        answer = 0
        visited = set()
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                visited.add((row, col))
                
                for dx, dy in directions:
                    newr, newc = row + dx, col + dy
                    if (newr, newc) not in visited:
                        if 0 <= newr < m and 0 <= newc < n:
                            
                            if grid[newr][newc] == 0:
                                visited.add((newr, newc))
                                q.append((newr, newc))
                            else:
                                return answer
            answer += 1
            
        return answer
        
        
                                
            
            
            
        
            
            
            