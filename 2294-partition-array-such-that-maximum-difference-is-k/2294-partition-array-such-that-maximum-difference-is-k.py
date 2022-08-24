class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        cur_min = nums[0]
        ans = 1
        for idx in range(1, len(nums)):
            if abs(nums[idx] - cur_min) > k:
                ans += 1
                cur_min = nums[idx]
        return ans
            
        