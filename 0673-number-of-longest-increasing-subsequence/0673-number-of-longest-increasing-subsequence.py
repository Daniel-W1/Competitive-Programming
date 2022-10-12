class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        dp2= [1]*n

        for j in range(n):
            for i in range(j):
                if nums[j] > nums[i]:
                    if dp[j] < 1+dp[i]:
                        dp[j] = 1+dp[i]
                        dp2[j] = dp2[i]
                    elif dp[j] == 1+dp[i]:
                        dp2[j] += dp2[i]

        ans = 0
        max_subs = max(dp)
        for i in range(len(dp2)):
            if dp[i] == max_subs:
                ans += dp2[i]

        return ans
