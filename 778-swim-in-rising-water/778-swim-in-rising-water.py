class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m = len(grid)-1
        bound = lambda r: r >= 0 and r <= m
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        heap = [(grid[0][0], 0, 0)]
        answer = 0
        visited = set()
        
        while heap:
            height, row, col = heappop(heap)
            answer = max(answer, height)
            if row == m and col == m:
                return answer
        
            for dx, dy in directions:
                newrow, newcol = row + dx, col + dy
                if bound(newrow) and bound(newcol) and (newrow, newcol) not in visited:
                    heappush(heap, (grid[newrow][newcol], newrow, newcol))
                    visited.add((newrow, newcol))
        