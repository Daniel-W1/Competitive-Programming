class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        score = 0
        nums.sort()

        prev = nums[0]
        for i in range(1, len(nums)):
            cur = nums[i]
            if cur <= prev:
                change = prev - cur
                cur += (change + 1)
                score += (change + 1)
            prev = cur
        return score
            
                
                
        
                    
                    
        
        
                    
                    
                
                
        
    
                    
    
        