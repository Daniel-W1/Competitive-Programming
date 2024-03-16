class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
            [0,0,1,0,1,1,0]
            
            {
                (0, 0): -1,
                (1, 0): -1,
            }
        """
                
        prefix = {
            0: -1,
        }
        
        ans = 0
        count = 0
        
        for idx, val in enumerate(nums):
            count += val
            zeros = idx - count + 1
            
            if count - zeros in prefix:
                ans = max(ans, idx - prefix[count - zeros])
            
            if count - zeros not in prefix:
                prefix[count - zeros] = idx
        
        return ans
            