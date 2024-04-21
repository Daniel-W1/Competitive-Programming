class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
            
        q = deque([source])
        visited = [False for _ in range(n+1)]
        visited[source] = True
        
        while q:
            node = q.popleft()
            
            if node == destination: return True

            for neig in graph[node]:
                if not visited[neig]:
                    visited[neig] = True
                    q.append(neig)
        
        return False
                    