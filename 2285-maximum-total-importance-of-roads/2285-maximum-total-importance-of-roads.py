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
        helper = [-len(val) for val in graph.values()]
        heapq.heapify(helper)
        length = len(helper)
        answer,max_value = 0,n
        for _ in range(length):
            answer += -(max_value*(heapq.heappop(helper)))
            max_value -= 1
        return answer