class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(set)
        blue = defaultdict(set)
        
        for n1, n2 in redEdges:
            red[n1].add(n2)
        
        for n1, n2 in blueEdges:
            blue[n1].add(n2)
            
        visited = set()
        distance = [float('inf') for _ in range(n)]
        def bfs(start,color):
            q = deque([(start, color, 0)])
            dist = 0
            while q:
                for _ in range(len(q)):
                    cur, color, dist = q.popleft()
                    visited.add((cur, color))
                    distance[cur] = min(distance[cur], dist)

                    if color != "r":
                        for neigh in red[cur]:
                            if (neigh, "r") not in visited:
                                q.append((neigh, "r", dist+1))
                    if color != "b":
                        for neigh in blue[cur]:
                            if (neigh, "b") not in visited:
                                q.append((neigh, "b", dist+1))
        
            for idx, val in enumerate(distance):
                if val == float('inf'):
                    distance[idx] = -1
                    
        bfs(0, -1)
        return distance
                
                    
                    
                
                
            