class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res =  1
        ans = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                res += 1
            else:
                res = 1
            ans = max(ans,res)
        return ans
            