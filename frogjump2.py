class Solution:
    def maxJump(self, stones: List[int]) -> int:
        """
        [1, 2, 3, 4, 5]
        """
        cur = stones[1] - stones[0]
        
        for idx in range(2, len(stones)):
            cur = max(cur, stones[idx] - stones[idx-2])
            
        return cur
                
