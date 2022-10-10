class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for n1, n2, w in times:
            graph[n1].append((n2, w))
        
        heap = [(0, k)]
        ans = -float('inf')
        visited = set()
        
        while heap:
            time, cur = heappop(heap)
            ans = max(ans, time)
    
            visited.add(cur)
            
            if len(visited) == n:
                return ans
            
            for neigh, w in graph[cur]:
                if neigh not in visited:
                    heappush(heap, (time + w, neigh))
        
        return -1

        