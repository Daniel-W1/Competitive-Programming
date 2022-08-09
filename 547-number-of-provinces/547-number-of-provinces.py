class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def createGraph(conn):
            graph = {}
            for i, con in enumerate(conn):
                for index in range(len(con)):
                    if con[index] == 1:
                        graph[i+1] = graph.get(i+1, [])
                        if index + 1 != i+1:
                            graph[i+1].append(index + 1)
            return graph
        graph = createGraph(isConnected)
        def dfs(node, visited):
            if node in visited:
                return 
            visited.add(node)
            for n in graph[node]:
                dfs(n, visited)
                
        visited = set()
        cnt = 0
        for node in graph:
            if node not in visited:
                dfs(node, visited)
                cnt += 1
        return cnt
