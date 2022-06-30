class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # []
        # [1,6]
        # [1,4,5,10] 5, 10  or 4, 10
        nums.sort()
        mid_value = nums[len(nums)//2]
        return sum(abs(val-mid_value) for val in nums)
    
        