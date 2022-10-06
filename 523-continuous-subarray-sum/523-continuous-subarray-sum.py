class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = {0:-1}
        
        cursum = 0
        for idx, num in enumerate(nums):
            cursum += num
            if cursum % k in prefix and idx - prefix[cursum%k] >= 2:
                return True
            
            if cursum %k not in prefix:
                prefix[cursum % k] = idx
            
            
        return False
                