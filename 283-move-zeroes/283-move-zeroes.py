class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1
                
                #[24,18,70,19,4,50,20,15,16,23,51,60]           
                #[24,18,19,4,20,15,16,23,60,51,70,50]
                