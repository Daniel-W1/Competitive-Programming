class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        nums = [str(num) for num in nums]
        for i,num in enumerate(nums):
            new = ""
            for n in num:
                new += str(mapping[int(n)])
            nums[i] = (int(new), i, num)
        return [int(val[2]) for val in sorted(nums)]