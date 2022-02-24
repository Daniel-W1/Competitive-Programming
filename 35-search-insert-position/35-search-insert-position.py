class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0 
        h = len(nums)-1
        while l < h and h-l > 1:
            mid = (l+h)//2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] < target:
                    l = mid
                else: h = mid
        if target <= nums[l]: return l
        elif target > nums[l] and target <= nums[h]: return h
        elif target == nums[l]: return l
        else: return h+1
        
        
               
            
            
        
       
        
                    
                    
            