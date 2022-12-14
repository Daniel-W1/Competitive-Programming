class Solution:
    def rob(self, nums: List[int]) -> int:
       # time O(n), space O(n), space can be optimised to O(1)
        prev1 = nums[0]
        prev2 = -1
        cur = nums[0]
        
        for idx in range(1, len(nums)):
            if idx > 1:
                cur = max(prev2 + nums[idx], prev1)
            else:
                cur = max(nums[idx], prev1)
            prev1, prev2 = cur, prev1
            
        return cur
        # time O(n), space O(1)