class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ans = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    q = deque([(r, c)])
                    grid[r][c] = "*"
                    
                    while q:
                        row, col = q.popleft()
                        
                        for dx, dy in directions:
                            new_r, new_c = row + dx, col + dy
                        
                            if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
                                if grid[new_r][new_c] == 1:
                                    q.append((new_r, new_c))
                                    grid[new_r][new_c] = "*"
                                elif not grid[new_r][new_c]:
                                    ans += 1
                            else:
                                ans += 1
            
        return ans
                        