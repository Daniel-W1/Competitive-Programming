class Solution:
    def atMostK(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        left = ans = 0
        
        for right in range(len(nums)):
            cnt[nums[right]] += 1
            
            while len(cnt) > k:
                cnt[nums[left]] -= 1
                
                if not cnt[nums[left]]:
                    del cnt[nums[left]]
                
                left += 1
            
            ans += right - left + 1
        
        return ans
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k-1)