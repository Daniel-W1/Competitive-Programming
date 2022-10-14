class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for c1, c2 in relations:
            graph[c1].append(c2)
            indegree[c2] += 1
        
        q = deque([])
        dist = [time[idx] for idx in range(n)]
        
        for node in range(1, n+1):
            if indegree[node] == 0:
                q.append(node)
        
        ans = 0
        curmax = 0
        while q:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                
                for neigh in graph[cur]:
                    dist[neigh-1] = max(dist[cur-1] + time[neigh-1], dist[neigh-1])
                    indegree[neigh] -= 1
                
                    if indegree[neigh] == 0:
                        q.append(neigh)
            ans += curmax
            curmax = 0
        
        return max(dist)
        
        
        