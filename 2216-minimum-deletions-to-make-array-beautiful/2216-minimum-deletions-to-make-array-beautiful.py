class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        deleted_count = 0
        i,j = 0,0
        while j < len(nums):
            number = nums[j]
            i = j-deleted_count
            if i%2 == 0 and j+1 < len(nums) and nums[j+1] == number:
                h = j + 1
                while h < len(nums) and number == nums[h]:
                    deleted_count += 1
                    h += 1
                j = h
                continue
            j += 1
            
        return deleted_count if not (len(nums)-deleted_count)%2 else deleted_count + 1
    