class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans_table = [1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    ans_table[i] = max(ans_table[i],ans_table[j]+1)
        return max(ans_table)
            