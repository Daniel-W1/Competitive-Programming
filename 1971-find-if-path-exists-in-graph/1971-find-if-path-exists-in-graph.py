class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.graph = self.create_graph(edges)
        def dfs(src,dst, visited = set()):
            if src == dst:
                return True
            if src in visited: return False
            visited.add(src)
            for neighbor in self.graph[src]:
                if dfs(neighbor,dst,visited):
                    return True

        return dfs(source,destination)
    def create_graph(self, edges):
        graph = {}
        for edge in edges:
            first = edge[0]
            second = edge[1]
            
            graph[first] = graph.get(first,[])
            graph[first].append(second)
            graph[second] = graph.get(second,[])
            graph[second].append(first)
        return graph
    
        