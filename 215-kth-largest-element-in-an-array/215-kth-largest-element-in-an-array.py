class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-val for val in nums]
        while True:
            heapq.heapify(nums)
            max_val = nums.pop(0)
            k -= 1 
            if not k:
                return -max_val
        
        
        