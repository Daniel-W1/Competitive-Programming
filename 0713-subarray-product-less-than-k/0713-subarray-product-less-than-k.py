class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = ans = 0
        run_prod = 1
        
        for right in range(len(nums)):
            run_prod *= nums[right]

            while run_prod >= k and left < len(nums):
                run_prod /= nums[left]
                left += 1
            
            ans += (right - left + 1)
        
        return max(ans, 0)