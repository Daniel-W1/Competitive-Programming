class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        q = deque([source])
        visited = set()
        visited.add(source)
        
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                
                if cur == destination: return True
                
                for neighbor in graph[cur]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
        
        return False
                        