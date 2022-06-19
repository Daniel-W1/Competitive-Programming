class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return self.create_graph(edges)
        
    def create_graph(self,edges):
        graph = {}
        for edge in edges:
            first = edge[0]
            second = edge[1]
            graph[first] = graph.get(first,[])
            graph[first].append(second)
            graph[second] = graph.get(second,[])
            graph[second].append(first)
            
            if len(graph[first]) == len(edges):
                return first
            if len(graph[second]) == len(edges):
                return second
    