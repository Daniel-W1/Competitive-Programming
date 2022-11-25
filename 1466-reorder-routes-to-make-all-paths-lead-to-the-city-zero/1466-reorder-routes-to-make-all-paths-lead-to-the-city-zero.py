class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for n1, n2 in connections:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        edges = set([tuple(edge) for edge in connections])
        visited = [False for _ in range(n)]
        q = deque([0])
        visited[0] = True
        count = 0
        
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                
                for neig in graph[cur]:
                    if visited[neig]: continue
                    if (neig, cur) not in edges:
                        count += 1
                    
                    visited[neig] = True
                    q.append(neig)
        
        return count
                    