class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # so this is obvious dijkstra problem, let's just do it and see how it goes
        n, m = len(grid), len(grid[0])
        distance = {(r, c) : float('inf') for r in range(n) for c in range(m)}
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        
        queue = deque([(0, 0, 0)])
        
        while queue:
            dist, row, col = queue.popleft()
            visited.add((row, col))
            
            # check the end
            if row == n-1 and col == m-1:
                return dist
            
            if dist > distance[row, col]: continue
            
            distance[row, col] = dist
            
            for idx, (dx, dy) in enumerate(directions):
                newr, newc = row + dx, col + dy
                
                if 0 <= newr < n and 0 <= newc < m:
                    if (newr, newc) not in visited:
                        cost = dist + int(idx + 1 != grid[row][col])
                        
                        if distance[newr, newc] > cost:
                            distance[newr, newc] = cost
                            
                            if cost > dist:
                                queue.append((cost, newr, newc))
                            else:
                                queue.appendleft((cost, newr, newc))
                            