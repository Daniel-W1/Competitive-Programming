class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        '''
        so the way am thinking to solve this problem is bfs
        q [ start ]
        q [i+arr[i], q-arr[i]]
        
        5
        4, 6
        1,4
        5,1
        '''
        q = collections.deque([start])
        seen = set()
        seen.add(start)
        while q:
            cur_size = len(q)
            for _ in range(cur_size):
                idx = q.popleft()
                if arr[idx] == 0:
                    return True
                left, right = idx - arr[idx], idx + arr[idx]
                if left >= 0 and left not in seen:
                    q.append(left)
                    seen.add(left)
                if right < len(arr) and right not in seen:
                    q.append(right)
                    seen.add(right)
        return False
        # time comp O(n), space O(n)
         
    