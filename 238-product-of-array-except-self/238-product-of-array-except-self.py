class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        O(n) time without using any division operation right
        
        prefix and suffix array
        let's look at what the prefix array would look like
        [1, 2, 6, 24]
        [ 24, 24,12,4]
        
        so when i don't use a number the result is just the prefix before that
        number time the suffix after that number because those totaly isolate the number
        
        '''
        prefix = [nums[0]]*len(nums)
        for idx in range(1, len(nums)):
            prefix[idx] = nums[idx]*prefix[idx-1]
        
        suffix = [nums[-1]]*len(nums)
        for idx in range(len(nums)-2, -1, -1):
            suffix[idx] = nums[idx]*suffix[idx+1]
        
        ans = [0]*len(nums)
        for idx in range(len(nums)):
            left = prefix[idx-1] if idx -1 >=0 else 1
            right = suffix[idx+1] if idx + 1 < len(nums) else 1
            ans[idx] = left * right
        return ans