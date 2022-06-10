class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        premins = [0]*len(nums)
        postmaxs = [0]*len(nums)
        prevmin = nums[0]
        prevmax = nums[-1]
        
        for i in range(len(nums)):
            premins[i] = min(prevmin,nums[i])
            prevmin = premins[i]
        for i in range(len(nums)-1,-1,-1):
            postmaxs[i] = max(prevmax,nums[i])
            prevmax = postmaxs[i]
        for i in range(1,len(nums)-1):
            if premins[i-1] <nums[i] < postmaxs[i+1]:
                return True
        return False
            