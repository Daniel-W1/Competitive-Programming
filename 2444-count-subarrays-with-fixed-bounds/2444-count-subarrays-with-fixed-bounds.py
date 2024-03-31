class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        """
            nums = [1,3,0,5,2,1,7,5], minK = 1, maxK = 5
        
        """
        left = min_cnt = max_cnt = ans = cur_cnt = 0
        
        for right in range(len(nums)):
            if nums[right] < minK or nums[right] > maxK:
                left = right + 1
                min_cnt = max_cnt = cur_cnt = 0
                continue
            
            min_cnt += nums[right] == minK
            max_cnt += nums[right] == maxK
            
            if min_cnt and max_cnt:
                while (min_cnt > 1 or nums[left] != minK) and not (nums[left] == maxK and max_cnt == 1):
                    cur_cnt += 1
                    min_cnt -= nums[left] == minK
                    max_cnt -= nums[left] == maxK
                    left += 1
                
                while (max_cnt > 1 or nums[left] != maxK) and not (nums[left] == minK and min_cnt == 1):
                    cur_cnt += 1
                    max_cnt -= nums[left] == maxK
                    left += 1
                
                ans += cur_cnt + 1
        
        return ans