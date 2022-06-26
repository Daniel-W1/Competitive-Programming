class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # first let's find the min and the_max and their index
        the_max = (-float('inf'),-1)
        the_min = (float('inf'),-1)
        for i,number in enumerate(nums):
            if number > the_max[0]:
                the_max = (number,i)
                
            if number < the_min[0]:
                the_min = (number,i)
        return min(max(the_max[1],the_min[1])+1,len(nums)-min(the_max[1],the_min[1]),min(the_max[1],the_min[1])+1+len(nums)-max(the_max[1],the_min[1]))
        
        
                