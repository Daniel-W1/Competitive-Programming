class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        while r > l+1:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        first_point = l if nums and nums[l]==target else r
        if not nums or nums[first_point] != target:
            return [-1,-1]
        l = first_point
        r = len(nums)-1
        while r > l+1:
            mid = (l+r)//2
            if nums[mid] == target:
                l = mid
            else:
                r = mid
        end_point = r if nums[r] == target else l
        return [first_point, end_point]
            