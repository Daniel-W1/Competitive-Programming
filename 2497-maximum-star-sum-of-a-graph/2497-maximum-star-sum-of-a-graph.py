class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
            
        n = len(vals)
        visited = [False for _ in range(n)]
        answer = -10**9 + 7
        
        def bfs(node):
            nonlocal answer
            
            q = deque([node])
            visited[node] = True
            while q:

                for _ in range(len(q)):
                    cur = q.popleft()


                    minheap = []

                    for neighbor in graph[cur]:

                        if len(minheap) < k:
                            heappush(minheap, vals[neighbor])
                        else:
                            heappushpop(minheap, vals[neighbor])

                        if not visited[neighbor]:
                            visited[neighbor] = True
                            q.append(neighbor)

                    # get the top k
                    cur_sum = vals[cur]

                    for _ in range(k):
                        if not minheap:
                            break
                        
                        if minheap[0] <= 0:
                            heappop(minheap)
                            continue
                            
                        cur_sum += heappop(minheap)

                    answer = max(answer, cur_sum)

        for node in range(n):
            if not visited[node]:
                bfs(node)
        
        return answer

                        