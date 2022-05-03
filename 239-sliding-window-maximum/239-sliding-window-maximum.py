class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = 0
        ans = []
        maxq = collections.deque([])
        while h != k:
            while maxq and nums[h] > maxq[-1][0]:
                maxq.pop()
            maxq.append((nums[h], h))
            h += 1
        ans.append(maxq[0][0])
        
        l=0
        while h < len(nums):
            while maxq and nums[h] > maxq[-1][0]:
                maxq.pop()
            maxq.append((nums[h], h))
            l += 1
            if l-1 == maxq[0][1]:
                maxq.popleft()
            ans.append(maxq[0][0])
            h += 1
        return ans
            
        
            
            
                    
        
        
            
            
            