class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums)
        
        
        while left <= right:
            mid = (left + right)//2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            
            if cnt > mid:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
                
        