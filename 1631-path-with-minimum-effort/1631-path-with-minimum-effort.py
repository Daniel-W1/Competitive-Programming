class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        n, m = len(grid), len(grid[0])
        heap = [(0, 0, 0)]
        distance = {(r, c) : float('inf') for r in range(n) for c in range(m)}
        visited = set()
        
        while heap:
            dist, row, col = heappop(heap)
            visited.add((row, col))
            
            if row == n-1 and col == m-1: return dist
            
            if distance[row, col] < dist: 
                continue
            
            for dx, dy in directions:
                new_r, new_c = row + dx, col + dy
                
                if 0 <= new_r < n and 0 <= new_c < m:
                    if (new_r, new_c) not in visited:
                        new_dist = max(dist,abs(grid[new_r][new_c] - grid[row][col]))
                        if new_dist < distance[new_r,new_c]:
                            distance[new_r, new_c] = new_dist
                            heappush(heap, (new_dist, new_r, new_c))
                            # print(heap)
                    
        return 0
        