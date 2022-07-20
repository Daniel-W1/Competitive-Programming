class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted([str(num) for num in nums], reverse = True)
        if nums[0] == "0": return "0"
        for i in range(len(nums)):
            num = nums[i]
            while i > 0 and str(nums[i])+str(nums[i-1]) >  str(nums[i-1])+str(nums[i]):
                nums[i], nums[i-1] = nums[i-1], nums[i]
                i -= 1
        return "".join(nums)
            