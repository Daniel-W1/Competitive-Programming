class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, h = 0, 0
        runningsum = 0
        minlen = len(nums)
        check = False
        while h < len(nums):
            while h < len(nums) and runningsum <= target:
                runningsum += nums[h]
                if runningsum >= target:
                    break
                h += 1
            if runningsum >= target:
                minlen = min(minlen, h-l+1)
                check = True
            while runningsum > target:
                runningsum -= nums[l]
                l += 1
                if runningsum >=  target:
                    minlen = min(minlen, h-l+1)
            h += 1
        return minlen if check else 0
            
            
            