class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        cursum = 0
        
        for i in range(len(nums)):
            if cursum == sum(nums[i+1:]):
                return i
            cursum += nums[i]
        return -1