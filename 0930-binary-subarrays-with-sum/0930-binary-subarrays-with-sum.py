class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        running_sum = 0
        ans = 0
        
        for val in nums:
            running_sum += val
            ans += prefix[running_sum - goal]
            prefix[running_sum] += 1
        
        return ans