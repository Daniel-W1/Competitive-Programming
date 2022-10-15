class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        
        graph = defaultdict(set)
        
        for n1, n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)
            
        # collect the leaves
        leaves = deque([])
        remaining = n
        for node in graph:
            if len(graph[node]) == 1:
                leaves.append(node)
                
        while remaining > 2:
            remaining -= len(leaves)
            newleaves = deque([])
            
            while leaves:
                cur = leaves.popleft()
                
                for neigh in graph[cur]:
                    graph[neigh].remove(cur)
                    
                    if len(graph[neigh]) == 1:
                        newleaves.append(neigh)
            leaves = newleaves
        
        return leaves
            