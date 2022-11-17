class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        ans = 0
        graph = defaultdict(list)
        for n1, n2 in roads:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        visited = [False for _ in range(n)]
        max1, max2 = 0, 0
        
        for node in range(n):
            if not visited[node]:
                q = deque([node])
                visited[node]= True
                component = []
                max_seen = 0
                
                while q:
                    for _ in range(len(q)):
                        cur = q.popleft()

                        
                        cnt = len(graph[cur])
                        max_seen = max(max_seen, cnt)
                        
                        component.append((cur, cnt))
                        
                            
                        for neighbor in graph[cur]:
                            if not visited[neighbor] :
                                q.append((neighbor))
                                visited[neighbor] = True
                
                # print(component)
                for idx, (node, network) in enumerate(component):
                    for idx2 in range(idx + 1, len(component)):
                        node2, network2 = component[idx2]

                        if node2 in graph[node]:
                            ans = max(ans, network + network2 - 1)
                        else:
                            # print(node, node2)
                            ans = max(ans, network + network2)
                    
                    # print(ans)

                if max_seen > max1:
                    max2, max1 = max1, max_seen
                else:
                    max2 = max(max2, max_seen)
        
        return max(ans, max1 + max2)
        
                            
        
        