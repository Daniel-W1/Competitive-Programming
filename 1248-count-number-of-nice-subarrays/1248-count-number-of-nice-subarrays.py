class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        answer = 0
        odd = 0
        mididx = -1
        
        for right, num in enumerate(nums):
            if num & 1:
                odd += 1
            
            if odd == k and mididx < 0:
                mididx = right
            
            while odd > k:
                if nums[left] & 1:
                    odd -= 1
                answer += right - mididx
                left += 1
                
                if odd == k:
                    mididx = right
        
        while odd == k:
            if nums[left] & 1:
                odd -= 1
            answer += right - mididx + 1
            left += 1
            
        return answer