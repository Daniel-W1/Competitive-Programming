class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if  n == 1: return [0]
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
        
        leaves = []
        for node in graph:
            if indegree[node] == 1:
                leaves.append(node)
                n -= 1
        
        while n:
            new_leaves = []
            
            while leaves:
                cur_node = leaves.pop()

                for neigh in graph[cur_node]:
                    indegree[neigh] -= 1

                    if indegree[neigh] == 1:
                        new_leaves.append(neigh)
                        n -= 1
            
            leaves = new_leaves[:]
        
        return leaves