class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        
        the_min = {}
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        heap = [(grid[0][0], 0, 0)]
        n, m = len(grid), len(grid[0])
        distance = defaultdict(lambda : float('inf'))
        
        while heap:
            
            cur_dist, r, c = heappop(heap)
            
            if distance[r, c] < cur_dist: continue
            
            distance[r, c] = cur_dist
            visited.add((r, c))
            
            for dx, dy in directions:
                newr, newc = r + dx, c + dy
                
                if 0 <= newr < n and 0 <= newc < m:
                    if (newr, newc) not in visited:
                        
                        new_dist = max(grid[newr][newc], cur_dist)
                        
                        if new_dist < distance[newr, newc]:
                            distance[newr, newc] = new_dist
                            heappush(heap, (distance[newr, newc], newr, newc))
        
        vals = sorted(distance.values())
        ans = [-1] * len(queries)
        
        for idx, q in enumerate(queries):
            ans[idx] = bisect_left(vals, q)
        
        return ans
        
            
            
            
