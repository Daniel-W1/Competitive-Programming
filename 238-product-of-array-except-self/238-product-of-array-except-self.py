class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        ans = [1]*len(nums)
        pre, post = 1,1
        for i in range(len(nums)):
            prefix[i] = pre*nums[i]
            pre = prefix[i]
       
        
        for i in range(len(nums)-1, -1, -1):
            postfix[i] = post*nums[i]
            post = postfix[i]
        
        mul = 1
        for i in range(len(nums)):
            if i + 1 == len(nums):
                ans[i] = mul*1
            else:
                ans[i] = mul*postfix[i+1]
                mul = prefix[i]
        return ans
        
        