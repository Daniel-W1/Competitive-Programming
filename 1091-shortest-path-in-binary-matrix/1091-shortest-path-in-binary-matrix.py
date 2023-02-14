class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0]: return -1
        n, m  = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        visited = set()
        
        q = deque([(0, 0, 1)])
        visited.add((0, 0))
        
        
        while q:
            
            r, c, steps = q.popleft()
                
            # print(r, c, "here")
                
            if (r, c) == (n-1, m-1): return steps
                
            for dx, dy in directions:
                newr, newc = r + dx, c + dy
                
                if 0 <= newr < n and 0 <= newc < m:
                    if grid[newr][newc] == 0 and (newr, newc) not in visited:
                        visited.add((newr, newc))
                        q.append((newr, newc, steps + 1))
                
        return -1
            