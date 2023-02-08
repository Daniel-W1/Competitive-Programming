class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # we can just assume their is an edge between adjecent guys 
        
        graph = defaultdict(list)
        candidate = set()
        
        for num1, num2 in adjacentPairs:
            if num1 not in graph:
                candidate.add(num1)
            else:
                candidate.remove(num1)
                
            if num2 not in graph:
                candidate.add(num2)
            else:
                candidate.remove(num2)
            
            graph[num1].append(num2)
            graph[num2].append(num1)
            
            
        
        num1 = candidate.pop()
        ans = [num1]
        q = deque([num1])
        visited = set()
        visited.add(num1)
        while q:
            cur = q.popleft()
            for neig in graph[cur]:
                if neig not in visited:
                    ans.append(neig)
                    visited.add(neig)
                    q.append(neig)
        
        return ans
                    
            