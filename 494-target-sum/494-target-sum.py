class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def cntall(i,res):
            if (i,res) not in memo:
                if i > len(nums)-1:
                    return 1 if res == target else 0
                memo[i,res]= cntall(i+1, res-nums[i]) + cntall(i+1,res+nums[i])
            return memo[i,res]
        return cntall(0, 0)
                