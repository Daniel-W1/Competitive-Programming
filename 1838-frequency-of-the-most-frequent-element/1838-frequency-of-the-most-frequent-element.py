class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # so the first approach to this problem is we need to sort them and go through them from the start
        nums.sort()
        
        # [1,4,8,13] k = 5
        #  4, 4, 8
        # [1,4,6,8,9,12] 4
        #    | | 
        l, h = 0, 0
        maxLeng = 0
        while h < len(nums):
            while h < len(nums) and k >= 0:
                h += 1
                if h < len(nums):
                    k -= (h-l)*(nums[h]-nums[h-1])
            maxLeng = max(maxLeng, h-l)
            if h == len(nums): break
            while l < h and k < 0:
                k += nums[h] - nums[l]
                l += 1
        return maxLeng
    