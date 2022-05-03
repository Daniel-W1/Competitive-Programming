class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = 0
        ans = []
        minq = collections.deque([])
        while h != k:
            while minq and nums[h] > minq[-1][0]:
                minq.pop()
            minq.append((nums[h], h))
            h += 1
        ans.append(minq[0][0])
        print(minq)
        l=0
        while h < len(nums):
            while minq and nums[h] > minq[-1][0]:
                minq.pop()
            minq.append((nums[h], h))
            l += 1
            if l-1 == minq[0][1]:
                minq.popleft()
            ans.append(minq[0][0])
            h += 1
        return ans
            
        
            
            
                    
        
        
            
            
            