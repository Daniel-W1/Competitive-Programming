class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal_post = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal_post:
                goal_post = i
        return goal_post == 0
                
            















            
                
            
            