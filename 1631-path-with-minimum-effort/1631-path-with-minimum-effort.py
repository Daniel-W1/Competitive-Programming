class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = [(0, 0, 0)]
        ans = 0
        direction = [(1, 0),(0,1),(-1,0),(0,-1)]
        visited = set()
        m, n = len(heights), len(heights[0])

        
        while heap:
            diff, r, c = heappop(heap)
            ans = max(ans, diff)
            cur = heights[r][c]
            visited.add((r, c))
        
            if r == m-1 and c == n-1:
                return ans
            
            for dx, dy in direction:
                newr, newc = r+dx, c+dy
                if 0 <= newr < m and 0 <= newc < n and (newr, newc) not in visited:
                    heappush(heap, (abs(heights[newr][newc]-cur), newr, newc))

            