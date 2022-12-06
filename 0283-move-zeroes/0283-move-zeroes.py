class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        left = 0
        n = len(nums)
        
        for right in range(n):
            if not nums[left] and nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
            
            if nums[left] != 0:
                left += 1
                
            