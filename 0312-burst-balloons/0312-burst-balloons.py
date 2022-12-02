class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
            [3, 1, 5, 8]
            
            |   |   |
            
        """
        
        nums = [1] + nums + [1]
        @cache
        def dp(left, right):
            if left > right:
                return 0
            
            res = 0
            for idx in range(left, right+1):
                score = nums[left-1] * nums[idx] * nums[right+1]
                score += dp(left, idx-1) + dp(idx+1, right)
                
                res = max(res, score)
            
            return res
        
        return dp(1, len(nums)-2)