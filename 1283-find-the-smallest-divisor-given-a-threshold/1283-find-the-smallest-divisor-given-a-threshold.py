class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        l, h = 1, nums[-1]
        while l <= h:
            mid = (l+h)//2
            cursum = 0
            for val in nums:
                cursum += math.ceil(val/mid)
            if cursum > threshold:
                l = mid + 1
            else:
                h = mid - 1
        return l
                