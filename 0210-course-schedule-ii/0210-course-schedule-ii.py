class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        grayset = set()
        blackset = set()
        
        graph = defaultdict(list)
        # first build the graph
        for c1, c2 in prerequisites:
            graph[c1].append(c2)
        
        ans = []
        def dfs(node):
            nonlocal ans
            if node in grayset:
                return False
            
            grayset.add(node)
            for neigh in graph[node]:
                if neigh in blackset:
                    continue
                res = dfs(neigh)
                if not res:
                    return False
            
            grayset.remove(node)
            blackset.add(node)
            ans.append(node)
            return True
        
        for node in range(numCourses):
            if node not in blackset:
                res = dfs(node)
                if not res:
                    return []
        
        return ans