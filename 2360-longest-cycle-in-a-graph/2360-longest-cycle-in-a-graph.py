class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        node_idx = [float('inf') for _ in range(n)]
        visited = [False for _ in range(n)]
        
        def dfs(node, curidx):
            if edges[node] == -1 or visited[node]: 
                return 0
            
            if node_idx[node] < curidx:
                return curidx - node_idx[node]
            
            node_idx[node] = curidx
            
            
            res = dfs(edges[node], curidx + 1)
            visited[node] = True
            
            return res
        
        ans = 0
        for node in range(n):
            ans = max(ans, dfs(node, 0))
        

        return ans if ans else -1
        
        
            
        
            
        
        