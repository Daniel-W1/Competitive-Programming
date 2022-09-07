class Solution:
    def minJumps(self, arr: List[int]) -> int:
        inds = collections.defaultdict(list)
        for idx, val in enumerate(arr):
            inds[val].append(idx)
        
        seen = set()
        q = collections.deque([(0, 0)])
        visited = set()
        
        # print(inds)
        while q:
            dist, idx = q.popleft()
            left,right = idx-1, idx+1
            visited.add(idx)
            # print("here", arr[idx],heap)
            if idx == len(arr)-1:
                return dist
            
            if left >= 0 and left not in visited:
                q.append((dist+1, left))
            if right < len(arr) and right not in visited:
                q.append((dist+1, right))
                
            if arr[idx] not in seen:
                for ind in inds[arr[idx]]:
                    if idx != ind and ind not in visited:
                        q.append((dist+1, ind))
                        visited.add(ind)
            seen.add(arr[idx])