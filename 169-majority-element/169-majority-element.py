class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        candidate = None
        
        for num in nums:
            if not candidate or cnt == 0:
                candidate = num
                cnt += 1
            else:
                if num == candidate: cnt = cnt + 1
                else: cnt = cnt - 1
        return candidate