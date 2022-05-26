class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        divs = [val for val in range(1,nums[-1]+1)]
        l, h = 0, len(divs)-1
        while l <= h:
            mid = (l+h)//2
            cursum = 0
            div = divs[mid]
            for val in nums:
                cursum += math.ceil(val/div)
            if cursum > threshold:
                l = mid+1
            else:
                h = mid - 1
        return divs[l]
                