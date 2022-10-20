class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor in color:
                    if color[neighbor] == color[node]:
                        return False
                
                else:
                    color[neighbor] = 1 - color[node]
                    check = dfs(neighbor)
                    
                    if not check:
                        return False
                    
            return True
        
        for node in range(len(graph)):
            if node not in color:
                color[node] = 1
                res = dfs(node)
                
                if not res:
                    return False
            
        return True
        
                        