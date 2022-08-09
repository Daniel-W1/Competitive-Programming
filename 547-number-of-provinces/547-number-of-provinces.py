class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # this is a very easy problem the only problem
        # creating the adjcency list and i can do that
        graph = {}
        visited  = set()
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1 and (i,j) not in visited:
                    if i+1 not in graph:
                        graph[i+1] = []
                    if j + 1 not in graph:
                        graph[j+1] = []
                    if i != j:
                        graph[i+1].append(j+1)
                        graph[j+1].append(i+1)
                    
                    visited.add((j,i))
        def dfs(node,visited):
            if node in visited: return
            visited.add(node)
            for n in graph[node]:
                dfs(n,visited)
        answer = 0
        for node in graph:
            if node not in visited:
                answer += 1
                dfs(node,visited)
        return answer
        