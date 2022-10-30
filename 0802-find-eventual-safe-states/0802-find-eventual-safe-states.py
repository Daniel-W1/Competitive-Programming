class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        queue = deque([])
        new_graph = defaultdict(list)
        indegrees = defaultdict(int)
        for node in range(len(graph)):
            if not graph[node]:
                queue.append(node)
            else:
                indegrees[node] = len(graph[node])
                # now let's reverse it
                for neighbor in graph[node]:
                    new_graph[neighbor].append(node)
        
        
        ans = []
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                ans.append(node)
                
                for neighbor in new_graph[node]:
                    indegrees[neighbor] -= 1
                    if not indegrees[neighbor]:
                        queue.append(neighbor)
        
        return sorted(ans)
                        
            