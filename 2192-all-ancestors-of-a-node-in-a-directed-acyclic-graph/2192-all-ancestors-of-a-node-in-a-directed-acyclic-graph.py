class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for n1, n2 in edges:
            graph[n1].append(n2)
            indegree[n2] += 1
        
        q = deque([])
        for node in range(n):
            if indegree[node] == 0:
                q.append(node)
        
        ans = [set() for _ in range(n)]
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                
                for neigh in graph[cur]:
                    indegree[neigh] -= 1
                    
                    if indegree[neigh] == 0:
                        q.append(neigh)
                        
                    for n in ans[cur]:
                        ans[neigh].add(n)
                    ans[neigh].add(cur)
    
        return [sorted(val) for val in ans]
            
        
        