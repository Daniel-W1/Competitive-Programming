class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        
        for num in count:
            if count[num-1]:
                ans = max(ans, count[num] + count[num-1])
            if count[num+1]:
                ans = max(ans, count[num] + count[num+1])
        
        return ans