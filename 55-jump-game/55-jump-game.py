class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal_post = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal_post:
                goal_post = i
        return goal_post == 0
                
            

    # so am trying to solve this thing with a dp 
    # and the first thing that came to mind is it's actually very similar
    # with the coin change problem with a little twist.
    # [2,3,1,1,4]
    # [3,2,1,0,4]
        fartherst_reach = nums[0]
        for i in range(1, len(nums)):
            if i > farthest_reach:
                return False
            farthest_reach = max(farthest_reach, i+nums[i])
        return True

        
        
    













            
                
            
            