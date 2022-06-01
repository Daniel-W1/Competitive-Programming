class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        prev = 0
        for i in range(len(nums)):
            prefix[i] = prev + nums[i]
            prev = prefix[i]
        return prefix