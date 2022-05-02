class Solution:
    # def longestSubarray(self, nums: List[int], limit: int) -> int:
#         maxlen = 0
#         i = 0
#         minQueue = collections.deque([])
#         maxQueue = collections.deque([])
#         for j in range(len(nums)):
#             while minQueue and minQueue[-1] > nums[j]:
#                 minQueue.pop()
#             minQueue.append(nums[j])
#             while maxQueue and maxQueue[-1] < nums[j]:
#                 maxQueue.pop()
#             maxQueue.append(nums[j])   
            
#             if maxQueue[0] - minQueue[0] <= limit:
#                 maxlen = max(maxlen, j-i+1)
#             else:
#                 if maxQueue[0] == nums[i]:
#                     maxQueue.popleft()
#                 if minQueue[0] == nums[i]:
#                     minQueue.popleft()
#                 i += 1
#         return maxlen
        def longestSubarray(self, nums: List[int], limit: int) -> int:
            # Deque
            maxd = collections.deque() # monotonically decreasing
            mind = collections.deque() # monotonically increasing
            i = 0
            for num in nums:
                # At each iteration, we maintain the biggest elements in maxd.
                # Remove any element smaller than num
                while len(maxd) and num > maxd[-1]:
                    maxd.pop()
                # At each iteration, we maintain the smallest elements in mind.
                # Remove any element bigger than num
                while len(mind) and num < mind[-1]:
                    mind.pop()
                # Why do we always add A[j] ?
                # As we will see below, we may have to remove an element(may be A[j-1] if i was j-1) from the beginning of the maxd/mind.
                # After that, we still need to know the max/min numbers from A[i/i+1]...A[j]
                maxd.append(num)
                mind.append(num)

                # maxd holds the biggest elements from A[i]...A[j] in decreasing order.
                # So maxd[0] is the biggest element in the window A[i]...A[j]
                # mind holds the smallest elements from A[i]...A[j] in increasing order.
                # So mind[0] is the smallest element in the window A[i]...A[j]
                # maxd[0]-mind[0] is the biggest difference in the window A[i]...A[j]
                if maxd[0] - mind[0] > limit:
                    # The biggest difference is over the limit; so remove A[i] from the window.
                    # Why do we check only maxd[0]/mind[0] to remove A[i]?
                    # Take maxd as an example. In order for A[i] to be present in maxd, 
                    # A[i] >= A[x], where x = i+1...j. In other words, it has to be the biggest element or 
                    # it would have already been removed. The biggest element would be in maxd[0]. 
                    if maxd[0] == nums[i]: maxd.popleft()
                    if mind[0] == nums[i]: mind.popleft()
                    # The new window for consideration is A[i+1]...A[j].
                    i += 1

            return len(nums) - i
    # Time: O(N)
    # Space: O(N)
        
                
                
                
                            
                        
                        
                    
                    