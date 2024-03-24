class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
            
            
        """
        left, right = 1, len(nums)-1
        ans = -1
        
        while left <= right:
            mid = (left + right)//2
            
            cnt = 0
            for val in nums:
                if val <= mid:
                    cnt += 1
            
            if cnt > mid:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans