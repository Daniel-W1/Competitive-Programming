class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, h = 0, 1
        while h < len(nums):
            if l < len(nums) and nums[l] != 0:
                l += 1
                h += 1
            else:
                if nums[h] == 0:
                    while h < len(nums) and nums[h] == 0:
                        h += 1
                    if h < len(nums):
                        nums[l], nums[h] = nums[h], nums[l]
                else:
                    nums[l], nums[h] = nums[h], nums[l]
                        
                
                