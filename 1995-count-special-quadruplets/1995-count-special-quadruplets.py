class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        
        cnt = {}
        ans = 0
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                ans += cnt.get(nums[j] - nums[i], 0)
                
            for k in range(i):
                cnt[nums[k] + nums[i]] = cnt.get(nums[k] + nums[i], 0) + 1
        
        return ans
                