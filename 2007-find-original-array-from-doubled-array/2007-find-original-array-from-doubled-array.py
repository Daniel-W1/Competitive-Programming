class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        queue,res=deque([]),[]
        
        for num in changed:
            if queue and queue[0]*2== num:
                other_num = queue.popleft()
                res.append(other_num)
            else:
                queue.append(num)
                
        return res if not queue else []