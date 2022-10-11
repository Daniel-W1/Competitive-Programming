class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        right = [0]*len(nums)
        right[-1] = nums[-1]
        
        for idx in range(len(nums)-2, -1 , -1):
            if nums[idx] < right[idx+1]:
                right[idx] = right[idx+1]
            else:
                right[idx] = nums[idx]

        prevmin = nums[0]
        for idx in range(1, len(nums)):
            if prevmin < nums[idx] < right[idx]:
                return True
            
            if prevmin > nums[idx]:
                prevmin = nums[idx] 
        
        return False
        
        