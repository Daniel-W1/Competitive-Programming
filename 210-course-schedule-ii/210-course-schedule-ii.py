class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premaps = {i:[] for i in range(numCourses)}
        for course,prereq in prerequisites:
            premaps[course].append(prereq)
        visited = set()
        self.ans = [-1]*numCourses
        self.index = numCourses-1
        visited = set()
        # here we need to use three sets that keep us from running in to cycles
        blackset = set()
        self.check = False
        def topsort(node,visited):
            if node in visited:
                self.check = True
                return
            visited.add(node)
            for n in premaps[node]:
                if n in blackset: continue
                topsort(n,visited)
            self.ans[self.index] = node
            self.index -= 1
            visited.remove(node)
            blackset.add(node)
            return
        for node in premaps:
            if node in blackset: continue
            topsort(node,visited)
            if self.check: return []
        return self.ans[::-1]
            
            
            