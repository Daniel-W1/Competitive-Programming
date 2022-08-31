class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[-1] - nums[0]
        
        for idx in range(len(nums)-1):
            num1, num2 = nums[idx], nums[idx+1]
            ans = min(ans, max(nums[-1] - k, num1+k) - min(nums[0]+k, num2 - k))
            
        return ans