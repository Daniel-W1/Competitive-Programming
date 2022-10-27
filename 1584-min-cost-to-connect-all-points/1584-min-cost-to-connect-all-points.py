class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # so let's try to do this problem using MST
        # first we need to build the graph
        
        manhattan = lambda p1, p2 : abs(p1[0]-p2[0]) + abs(p1[1] - p2[1])
        edges = []
        
        for idx in range(len(points)):
            for other in range(idx + 1, len(points)):
                p1, p2 = points[idx], points[other]
                edges.append((idx, other, manhattan(p1, p2)))
        
        parents = list(range(len(points)))
        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            
            return parents[node]
        
        cost = 0
        for idx1, idx2, weight in sorted(edges, key = lambda edge : edge[2]):
            p1, p2 = find(idx1), find(idx2)
            
            if p1 == p2:
                continue
            
            parents[p1] = p2
            cost += weight
        
        return cost
            
        

#         graph = defaultdict(list)
#         n = len(points)
#         manhattan = lambda p1, p2 : abs(p1[0]-p2[0]) + abs(p1[1] - p2[1])
        
#         for idx in range(n):
#             for other in range(idx + 1, n):
#                 graph[idx].append((manhattan(points[idx], points[other]), other))
#                 graph[other].append((manhattan(points[idx], points[other]), idx))
        
#         visited = set()
#         minheap = [(0, 0)]
#         ans = 0
        
#         while len(visited) < n:
#             cost, idx = heappop(minheap)
            
#             if idx in visited:
#                 continue
#             visited.add(idx)
#             ans += cost
            
#             for ncost, neighbor in graph[idx]:
#                 if neighbor not in visited:
#                     heappush(minheap, (ncost, neighbor))
        
#         return ans