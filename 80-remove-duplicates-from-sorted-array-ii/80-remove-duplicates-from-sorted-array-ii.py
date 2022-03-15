class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, h = 0, 1
        while h < len(nums):
            if nums[h] == nums[l]:
                l += 1
                nums[l] = nums[h]
                h += 1
            while h < len(nums) and nums[h] == nums[l]:
                h += 1
            l += 1
            if h == len(nums): return l
            nums[l] = nums[h]
            h += 1
        return l + 1
            
                