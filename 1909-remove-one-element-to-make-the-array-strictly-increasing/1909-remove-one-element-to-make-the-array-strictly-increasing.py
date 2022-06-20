class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def isstrict(nums):
            prev = nums[0]
            for i in range(1,len(nums)):
                if nums[i]-prev <= 0:
                    return False
                prev = nums[i]
            return True
        prev = nums[0]
        for i in range(1,len(nums)):
            if nums[i]-prev <= 0:
                return isstrict(nums[:i]+nums[i+1:]) or isstrict(nums[:i-1]+nums[i:])
            prev = nums[i]
        return True
    
            
                
                
            
            
                
            
            