class Solution:
    def rob(self, nums: List[int]) -> int:
        # ans = {}
        # ans[len(nums)-1], ans[len(nums)-2] = nums[len(nums)-1], max(nums[len(nums)-1], nums[len(nums)-2])
        # def smartrob(i):
        #     if i not in ans:
        #         ans[i] = max(smartrob(i+2) + nums[i], smartrob(i+1))
        #     return ans[i]
        # return smartrob(0)
    # lol this looks like a bottom up with recursion but let's do a real bottom up huh?
        ans = [0]*len(nums)
        if len(ans)<2:
            return nums[0]
        ans[0], ans[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            ans[i] = max(ans[i-2]+nums[i], ans[i-1])
        return ans[-1]
    
    