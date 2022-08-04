class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def divide(divisor):
            res = 0
            for num in nums:
                res += ceil(num/divisor)
            return res
        
        left, right = 1, max(nums)
        while left <= right:
            mid = (left + right)//2
            current_res = divide(mid)

            if current_res > threshold:
                left = mid + 1
            else:
                right = mid - 1
        return right+1
            
            
                