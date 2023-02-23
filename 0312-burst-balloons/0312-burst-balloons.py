class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        # so the idea is instead of bursting the ballon right away may be i can simulate
        # bursting the ballon at last 
        
        nums = [1] + nums + [1]
        
        @cache
        def dfs(left, right):
            
            if left > right:
                return 0
            
            
            res = 0
            for idx in range(left, right + 1):
                
                score = nums[left-1] * nums[idx] * nums[right + 1]
                
                score += dfs(left, idx - 1) + dfs(idx + 1, right)
                
                res = max(res, score)
            
            return res
        
        return dfs(1, len(nums)-2)
                
            