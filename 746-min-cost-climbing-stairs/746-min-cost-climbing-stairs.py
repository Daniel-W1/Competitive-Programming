class Solution:
    def minCostClimbingStairs(self, nums: List[int]) -> int:
#             if not cost:
#                 return 0
#             dp = [0] * len(cost)
#             dp[0] = cost[0]
#             if len(cost) >= 2:
#                 dp[1] = cost[1]
#             for i in range(2, len(cost)):
#                 dp[i] = cost[i] + min(dp[i-1], dp[i-2])

#             return min(dp[-1], dp[-2])
        memo = {}
        memo[len(nums)-1], memo[len(nums)-2] = nums[len(nums)-1], nums[len(nums)-2]
        def smart_min(i):
            if i not in memo:
                memo[i] = nums[i] + min(smart_min(i+1), smart_min(i+2))
            return memo[i]
        return min(smart_min(0), smart_min(1))

                
            
        