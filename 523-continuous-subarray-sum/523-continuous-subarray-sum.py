class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = {0:-1}
        
        cursum = 0
        for idx, num in enumerate(nums):
            cursum += num
            res = cursum % k
            if res in prefix and idx - prefix[res] >= 2:
                return True
            
            if res not in prefix:
                prefix[res] = idx
            
        return False
                