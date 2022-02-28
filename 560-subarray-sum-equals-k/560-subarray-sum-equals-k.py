class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum = 0
        ans = 0
        prefixSums = { 0:1 }
        
        for n in nums:
            curSum += n
            diff = curSum - k
            ans += prefixSums.get(diff,0)
            prefixSums[curSum] = prefixSums.get(curSum, 0) + 1
        return ans
            