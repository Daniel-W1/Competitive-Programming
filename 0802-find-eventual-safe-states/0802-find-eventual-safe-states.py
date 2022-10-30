class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        visited = set()
        safe = set()
        not_safe = set()

        def dfs(node):
            if node in visited:
                return False
            
            if not graph[node]:
                return True
            
            if node in safe or node in not_safe:
                return node in safe
            
            visited.add(node)
            check = True
            for neighbor in graph[node]:
                check = check and dfs(neighbor)
            
            visited.remove(node)
            if check: safe.add(node)
            else: not_safe.add(node)
            
            return check
        
        n = len(graph)
        for node in range(n):
            dfs(node)
            
            if not graph[node]:
                safe.add(node)
        
        return sorted(safe)
        
        
            
            