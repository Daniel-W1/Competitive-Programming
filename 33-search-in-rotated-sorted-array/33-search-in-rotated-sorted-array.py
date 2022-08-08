class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # we need to find the minimum number that is less that cur
        cur = nums[0]
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left + right)//2
            if nums[mid] >= cur:
                left = mid + 1
            else:
                right = mid - 1
        minimum = right + 1
        
        def binaryS(left, right):
            while left <= right:
                mid = (left + right)//2
                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        return max(binaryS(0, minimum-1), binaryS(minimum, len(nums)-1))