class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
    
        def helper(_sum, nums, start, end):
            
            if (start, end) in memo:
                return memo[(start, end)]
            
            if start == end:
                memo[(start, end)] = nums[start]
                return nums[start]
            
            score1 = _sum - helper(_sum - nums[start], nums, start+1, end) 
            score2 = _sum - helper(_sum - nums[end], nums, start, end-1)
            
            res = max(score1, score2)
            memo[(start, end)] = res
            
            return res
        
        return helper(sum(nums), nums, 0, len(nums)-1) * 2 >= sum(nums)
            