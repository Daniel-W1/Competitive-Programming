class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {}
        for course,pre in prerequisites:
            if course not in prereqs:
                prereqs[course] = []
            prereqs[course].append(pre)
        
        visited = set()
        
        def dfs(node,visited):
            if node in visited:
                return False
            if node not in prereqs:
                return True
            visited.add(node)
            for pre in prereqs[node]:
                res = dfs(pre,visited)
                if not res:
                    return False
            visited.remove(node)
            prereqs[node] = []
            return True
        for node in prereqs:
            res = dfs(node,visited)
            if not res:
                return False
        return True
        
            