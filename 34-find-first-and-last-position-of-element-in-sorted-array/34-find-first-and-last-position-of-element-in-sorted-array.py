class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left+right)//2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        start = right + 1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        end = left - 1
        
        return [start, end] if start <= end < len(nums) and nums[start] == nums[end] == target else [-1,-1]