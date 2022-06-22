class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        def buildgraph(roads):
            graph = {}
            for road in roads:
                if road[0] not in graph:
                    graph[road[0]] = []
                if road[1] not in graph:
                    graph[road[1]] = []
                    
                graph[road[0]].append(road[1])
                graph[road[1]].append(road[0])
            return graph
        graph = buildgraph(roads)
        helper = []
       
        for k,v in graph.items():
            helper.append((k,len(v)))
        helper.sort(key = lambda val:val[1],reverse = True)
        ans = 0
        max_value = n
        for val in helper:
            ans += max_value*val[1]
            max_value -= 1
        return ans