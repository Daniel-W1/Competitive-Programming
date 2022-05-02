class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        # for simplicity
        f,s = firstLen, secondLen
        
        # initialization: maxfirst, maxsecond, maxtotal
        maxf, maxs, maxt = nums[f-1], nums[s-1], nums[f+s-1]
        
        for i in range(f+s, len(nums)):
            # find the maximum subarray of length f
            maxf = max(maxf, nums[i-s] - nums[i-s-f])
            # find the maximum subarray of length s
            maxs = max(maxs, nums[i-f] - nums[i-f-s])
            # find the maximum subarray of length f+s
            maxt = max(maxt, 
                      max(maxf + nums[i]-nums[i-s], maxs + nums[i]-nums[i-f]))
        return maxt
            
            
        
        