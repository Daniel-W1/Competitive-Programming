class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new = nums.copy()
        print(new)
        for i, val in enumerate(new):
            index = i + k
            while index > len(new)-1: 
                index -= len(new)
            nums[index] = val
            