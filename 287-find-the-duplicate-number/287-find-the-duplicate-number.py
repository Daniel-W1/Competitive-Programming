class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i,val in enumerate(nums[:-1]):
            if nums[i+1] == nums[i]:
                return nums[i]