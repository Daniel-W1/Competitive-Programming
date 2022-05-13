class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        rangesum = 0
        for i in range(len(nums)):
            minn = nums[i]
            maxn = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] > maxn:
                    maxn = nums[j]
                elif nums[j] < minn:
                    minn = nums[j]
                rangesum += (maxn-minn)
        return rangesum
    
                    
                    
                    