class Solution:
    def canFinish(self, num: int, pre: List[List[int]]) -> bool:
        '''
        okay this is a good top sort question and let's solve it now
        
        0 -- > 1
        
        first how do we build the adj list for this question
        
        1 -- > 0 -- > 1
        '''
        graph = defaultdict(list)
        self.cycle = False
        for node1, node2 in pre:
            graph[node1].append(node2)
            
        visited = [False]*num
        res = []
        
        # print(graph)
        def topsort(node, seen):
            visited[node] = True
            seen.add(node)
            for neighbor in graph.get(node, []):
                if neighbor in seen:
                    self.cycle = True
                    return
                
                if not visited[neighbor]:
                    topsort(neighbor, seen)
                    
            seen.remove(node)
            res.append(node)
            
        for node in range(num):
            if not visited[node]:
                topsort(node, set())
        
        # print(res, self.cycle)
        # 0 -> 1
        '''
        0 --> 1 
        |
        2
        '''
        return len(res) == num and not self.cycle