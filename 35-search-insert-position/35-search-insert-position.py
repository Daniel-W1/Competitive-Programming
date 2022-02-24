class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        temp = nums
        while len(nums) > 1:
            mid = len(nums)//2
            if target == nums[mid]:
                return temp.index(nums[mid])
            else:
                if target < nums[mid]: nums = nums[:mid]
                else: 
                    nums = nums[mid:]
        
        if target > nums[0]: return temp.index(nums[0]) + 1
        else: return temp.index(nums[0])
            
        
       
        
                    
                    
            