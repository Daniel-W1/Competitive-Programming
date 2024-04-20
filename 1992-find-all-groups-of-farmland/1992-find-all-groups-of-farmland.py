class Solution:
    def findFarmland(self, grid: List[List[int]]) -> List[List[int]]:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ans = []
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    q = deque([(r, c)])
                    grid[r][c] = 0
                    
                    end = [r, c]
                    
                    while q:
                        row, col = q.popleft()
                        
                        for dx, dy in directions:
                            new_r, new_c = row + dx, col + dy
                        
                            if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == 1:
                                q.append((new_r, new_c))
                                grid[new_r][new_c] = 0
                                end[0] = max(end[0], new_r)
                                end[1] = max(end[1], new_c)
                
                    ans.append([r, c, end[0], end[1]])
            
        return ans