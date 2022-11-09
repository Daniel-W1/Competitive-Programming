class Solution:
    def findatmost(self, nums, k):
        left = 0
        ans = 0
        cnt = Counter()
        
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
        return self.findatmost(nums, k) - self.findatmost(nums, k-1)
    
    