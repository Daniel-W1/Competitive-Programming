class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        total = 0
        maxans = -float('inf')
        minans = float('inf')
        
        mincur, maxcur = 0, 0
        
        for val in nums:
            total += val
            maxcur += val
            mincur += val
            
            maxans = max(maxans, maxcur)
            minans = min(minans, mincur)
            
            maxcur = max(maxcur, 0)
            mincur = min(mincur, 0)
        
        return max(maxans, total - minans if total != minans else -float('inf'))
            
        
        