class Solution:
    def minCostClimbingStairs(self, nums: List[int]) -> int:
        # so what are the conditons for this problem
        # so reaching the last of the prev last index is considered as a 
        # so the best way to do this is just to call the function
        # twice for both the 0th and the 1st index
        # so the code below works but the quesion is how do we memoise it
        
        # let's sketch our decision tree on paper first
        # so from sketching it out we can obviously see that 
        # the index we are at can used as a key to memoise the code
        memo = {}
        def minCost(i):
            if i in memo: return memo[i]
            if i >= len(nums)-2:
                return nums[i]
            memo[i] = min(minCost(i+1)+nums[i], minCost(i+2)+nums[i])
            return memo[i]
        return min(minCost(0), minCost(1))
    
    