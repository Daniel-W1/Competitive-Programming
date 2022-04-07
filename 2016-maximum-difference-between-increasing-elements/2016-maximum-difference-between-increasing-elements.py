class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        i = 0
        dif = 0
        minimum = nums[i]
        while i < len(nums):
            if nums[i] > minimum:
                dif = max(dif, nums[i]-minimum)
            else:
                minimum = nums[i]
            i += 1
            
        return dif if dif else -1
            
            