class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # [2,4,6,8,9,10,15]
        # [1,2,4,3,5,6]
        
        # [1,2,3,4,5,6]
        # time comp = O(nlogn)
        # space comp = O(n)
        sorted_nums = sorted(nums)
        
        left,right = 0,len(nums)-1

        while left < right:
            if nums[left] != sorted_nums[left] and nums[right] != sorted_nums[right]:
                break
            if nums[left] == sorted_nums[left]:
                left += 1
            if nums[right] == sorted_nums[right]:
                right -= 1
            
           
        return right - left + 1 if right != left else 0
        
        
        