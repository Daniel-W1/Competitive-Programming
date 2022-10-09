class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)
        for n1, n2, p in flights:
            graph[n1].append((n2, p))
        
        # print(graph)
        visited  = [-1 for _ in range(n)]
        def shortest(src, dst, k):
            heap = [(0, src, k+1)]
            while heap:
                price, node, k = heappop(heap)
                    
                if k < 0:
                    continue
                
                if node == dst:
                    return price
                
                visited[node] = k
                
                for other, p in graph[node]:
                    if k > visited[other]:
                        heappush(heap, (p+price, other, k-1))
                # print(heap)
            
            return -1
        
        return shortest(src, dst, k)