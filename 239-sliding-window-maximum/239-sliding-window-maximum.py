class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        q = deque([])
        
        for right in range(k):
            while q and q[-1][0] <= nums[right]:
                q.pop()
            q.append((nums[right], right))
    
        ans = []
        for idx in range(right+1, len(nums)):
            # print(q)
            ans.append(q[0][0])
            left += 1
            while q and q[-1][0] <= nums[idx]:
                q.pop()
            q.append((nums[idx], idx))
            
            if q[0][1] < left:
                q.popleft()
                
        ans.append(q[0][0])
        return ans
    # time comp O(nlogk)
    # space O(n)
    # try the O(n) time sol tomorrow
            