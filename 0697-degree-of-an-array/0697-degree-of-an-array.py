class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        the_max = max(Counter(nums).values())
        n = len(nums)
        cnt = defaultdict(int)
        left = 0
        ans = inf
        
        for right in range(n):
            cnt[nums[right]] += 1
            
            while cnt[nums[right]] == the_max:
                ans = min(ans, right - left + 1)
                cnt[nums[left]] -= 1
                left += 1
        
        return ans 