class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxlen = 0
        i = 0
        minQueue = collections.deque([])
        maxQueue = collections.deque([])
        for j in range(len(nums)):
            while minQueue and minQueue[-1] > nums[j]:
                minQueue.pop()
            minQueue.append(nums[j])
            while maxQueue and maxQueue[-1] < nums[j]:
                maxQueue.pop()
            maxQueue.append(nums[j])   
            
            if maxQueue[0] - minQueue[0] <= limit:
                maxlen = max(maxlen, j-i+1)
            else:
                if maxQueue[0] == nums[i]:
                    maxQueue.popleft()
                if minQueue[0] == nums[i]:
                    minQueue.popleft()
                i += 1
        return maxlen
        
        
                
                
                
                            
                        
                        
                    
                    