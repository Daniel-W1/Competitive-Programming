class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        charset = set()
        ans,res,l = 0,0,0
        for i in range(len(nums)):
            while nums[i] in charset:
                charset.remove(nums[l])
                ans -= nums[l]
                l += 1
            ans += nums[i]
            charset.add(nums[i])
            res= max(res,ans)
        return res
            