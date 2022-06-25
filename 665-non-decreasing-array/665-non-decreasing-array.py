class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        def isnondec(arr):
            prev = arr[0]
            for i in range(1,len(arr)):
                if arr[i] - prev < 0:
                    return False
                prev = arr[i]
            return True
        prev = nums[0]
        for i in range(1,len(nums)):
            if nums[i] - prev < 0:
                return isnondec(nums[:i]+nums[i+1:]) or isnondec(nums[:i-1]+nums[i:])
            prev = nums[i]
        return True