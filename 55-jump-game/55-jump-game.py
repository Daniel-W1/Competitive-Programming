class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        g=n-1
        for i in range(n-1,-1,-1):
            if i+nums[i]>=g:
                g=i
        return g==0
            















            
                
            
            