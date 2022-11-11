class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        
        for idx in range(len(nums)-2):
            the_max = nums[idx+2]
            if the_max < nums[idx] + nums[idx+1]:
                ans = sum((the_max, nums[idx], nums[idx+1]))
        
        return ans