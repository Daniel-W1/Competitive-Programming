class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            j = i
            if nums[i] == val:
                while j < len(nums) and nums[j] == val:
                    j += 1
                if j == len(nums): j -= 1
                nums[i], nums[j] = nums[j], val
            i += 1
        i = 0
        if not nums: return 0
        while i < len(nums) and nums[i] != val:
            i += 1
        return i
                
                    
                
        