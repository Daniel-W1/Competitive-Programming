class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)-1):
            if not (i-cnt)%2 and nums[i]==nums[i+1]:
                cnt += 1
        return cnt if not (len(nums)-cnt)%2 else cnt+1