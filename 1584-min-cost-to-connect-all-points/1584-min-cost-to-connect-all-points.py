class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # so let's try to do this problem using MST
        # first we need to build the graph
        graph = defaultdict(list)
        n = len(points)
        manhattan = lambda p1, p2 : abs(p1[0]-p2[0]) + abs(p1[1] - p2[1])
        
        for idx in range(n):
            for other in range(idx + 1, n):
                graph[idx].append((manhattan(points[idx], points[other]), other))
                graph[other].append((manhattan(points[idx], points[other]), idx))
        
        visited = set()
        minheap = [(0, 0)]
        ans = 0
        
        while len(visited) < n:
            cost, idx = heappop(minheap)
            
            if idx in visited:
                continue
            visited.add(idx)
            ans += cost
            
            for ncost, neighbor in graph[idx]:
                if neighbor not in visited:
                    heappush(minheap, (ncost, neighbor))
        
        return ans