class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        dp = [[0]*26 for _ in range(n)]
        
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for n1, n2 in edges:
            graph[n1].append(n2)
            indegree[n2] += 1
        
        queue = deque([])
        for node in range(n):
            if not indegree[node]:
                queue.append(node)
        
        node_cnt = 0
        while queue:
            cur = queue.popleft()
            node_cnt += 1
            color_idx = ord(colors[cur]) - ord("a")
            dp[cur][color_idx] += 1
            
            for neighbor in graph[cur]:
                for idx, char in enumerate(dp[neighbor]):
                    dp[neighbor][idx] = max(dp[neighbor][idx], dp[cur][idx])
                
                indegree[neighbor] -= 1
                if not indegree[neighbor]:
                    queue.append(neighbor)
        
        return max(max(row) for row in dp) if node_cnt == n else -1
            
        
        
        
        