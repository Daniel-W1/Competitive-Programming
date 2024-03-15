class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            [1, 2, 6, 24]
            
            [1, 2, 3, 4]
            
            [0, 12,8,6]
        """
        n = len(nums)
        ans = [1]*n
        prefix = nums[0]
        suffix = nums[-1]
        
        for i in range(1, n-1):
            ans[i] *= prefix
            ans[n- i-1] *= suffix
            
            prefix *= nums[i]
            suffix *= nums[n - i - 1]
        
        ans[0] = suffix
        ans[-1] = prefix
        
        return ans
        
        