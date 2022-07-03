class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        l,r = 0,0
        max_len = 0
        while r < len(nums):
            while nums[r] - nums[l] > 1:
                l += 1
            if nums[r] - nums[l] == 1:
                max_len = max(max_len, r-l+1)
            r += 1
        return max_len
            
        