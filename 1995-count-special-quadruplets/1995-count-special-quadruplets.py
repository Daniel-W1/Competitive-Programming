class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ans = 0 
        freq = Counter()
        for i in range(len(nums)): 
            for j in range(i+1, len(nums)): ans += freq[nums[j] - nums[i]]
            for ii in range(i): freq[nums[ii] + nums[i]] += 1
        return ans