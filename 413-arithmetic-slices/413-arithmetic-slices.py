class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res = 0
        for l in range(0, len(nums)-2):
            h = l+1
            dif = nums[h]-nums[l]
            prev = nums[l]
            while h < len(nums) and nums[h]-prev == dif:
                if h - l + 1 >= 3:
                    res += 1
                prev = nums[h]
                h += 1

        return res
                