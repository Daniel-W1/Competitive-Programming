class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        heap = [(0, 0, 0)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = [[False for _ in range(m)] for _ in range(n)]
        visited[0][0] = True
        
        while heap:
            cur_cost, row, col = heappop(heap)
            
            if row == n-1 and col == m-1: return cur_cost

            for dx, dy in directions:
                new_r, new_c = row + dx, col + dy
                if 0 <= new_r < n and 0 <= new_c < m:
                    if not visited[new_r][new_c]:
                        cost = cur_cost + grid[new_r][new_c]
                        heappush(heap, (cost, new_r, new_c))
                        visited[new_r][new_c] = True 
                    
            
            
            
            
            