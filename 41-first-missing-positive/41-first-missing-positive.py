class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # okay first can u solve it in O(n) time using extra space
        check = [False]*len(nums)
        for num in nums:
            if num > 0 and num <= len(check):
                check[num-1] = True
        
        for idx in range(len(check)):
            if not check[idx]:
                return idx + 1
        return idx + 2