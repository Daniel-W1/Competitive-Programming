class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        a -- > b --> c
        bc -- > cd
        
        a/b = 2
        b = a/2
        b/c = 3
        a/c = 6
        
        '''
        graph = defaultdict(list)
        edge_meaning = {}
        
        for idx, (node1, node2) in enumerate(equations):
            graph[node1].append(node2)
            graph[node2].append(node1)
            
            edge_meaning[node1 + "," + node2] = values[idx]
            edge_meaning[node2 + "," + node1] = 1/values[idx]
        
        
        def bfs(node1, node2):
            visited = set()
            if node1 not in graph or node2 not in graph:
                return -1
            
            q = deque([(node1, 1)])
            while q:
                for _ in range(len(q)):
                    cur, res = q.popleft()
                    if cur == node2:
                        return res
                    
                    visited.add(cur)
                    for other in graph[cur]:
                        if other not in visited:
                            edge = cur + "," + other
                            q.append((other, res * edge_meaning[edge]))
                            
            return -1
        
        ans = []
        for node1, node2 in queries:
            ans.append(bfs(node1, node2))
        return ans
