class Solution:
    def dijkstra(self, n, graph):
        distance = [float('inf') for _ in range(n+1)]
        distance[n] = 0
        heap = [(0, n)]
        visited = [False for _ in range(n+1)]
        
        while heap:
            dist, node = heappop(heap)
            visited[node] = True
            
            # first optimisation is this
            if dist > distance[node]: continue
            
            for neig in graph[node]:
                if visited[neig]: continue
                
                current_distance = dist + graph[node][neig]
                if current_distance < distance[neig]:
                    distance[neig] = current_distance
                    heappush(heap, (current_distance, neig))
                # relaxing all the neighbor edges
            
        return distance
    
    def dfs(self, node , end, graph, distance):
        if node in self.memo: return self.memo[node]
        if node == end:
            return 1
        
        total = 0
        self.visited[node] = True
        
        for neig in graph[node]:
            if self.visited[neig]: continue
            if distance[neig] >= distance[node]: continue
            
            total += self.dfs(neig, end, graph, distance)
        
        self.visited[node] = False
        
        self.memo[node] = total
        return total % (10**9 + 7)
    
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(dict)
        self.memo = {}
        
        for n1, n2, w in edges:
            graph[n1][n2] = w
            graph[n2][n1] = w
        
        distance = self.dijkstra(n, graph)
        self.visited = [False for _ in range(n+1)]
        # print(distance)
            
        return self.dfs(1, n, graph, distance)