class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_jump = 0
        
        for idx, val in enumerate(nums):
            if idx > max_jump: return False
            max_jump = max(max_jump, idx + val)
        
        return True