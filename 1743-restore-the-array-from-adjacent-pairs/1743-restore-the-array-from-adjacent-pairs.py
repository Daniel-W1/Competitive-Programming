class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # we can just assume their is an edge between adjecent guys 
        
        graph = defaultdict(list)
        cnt = Counter()
        candidate = set()
        
        for num1, num2 in adjacentPairs:
            graph[num1].append(num2)
            graph[num2].append(num1)
            cnt[num1] += 1
            cnt[num2] += 1
            
            
        
        num1 = [val for val in cnt if cnt[val] == 1][0]
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
                    
            