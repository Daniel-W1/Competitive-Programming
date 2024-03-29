class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
            atleast K means,
            
            >= k
            
            total_subarray - atmost k = answer
        
        """
        the_max = max(nums)
        total_subarray = len(nums)*(len(nums)+1)/2
        left = ans = max_cnt = 0
        
        for right in range(len(nums)):
            max_cnt += nums[right] == the_max
            
            while max_cnt == k:
                max_cnt -= nums[left] == the_max
                left += 1
            
            ans += (right - left + 1)
        
        return int(total_subarray - ans)
            