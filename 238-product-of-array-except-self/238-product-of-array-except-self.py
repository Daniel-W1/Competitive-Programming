class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # okay here we go for the product array
        # first create the ans and use it to store bothe the prefix and suffix
        
        ans = [1]*len(nums)
        for idx in range(1, len(nums)):
            ans[idx] = nums[idx-1]*ans[idx-1]
        
        # now let's do the suffix part
        suffix_product = 1
        for idx in range(len(nums)-1, -1, -1):
            ans[idx] = suffix_product * ans[idx]
            suffix_product *= nums[idx]
        
        return ans
        '''
        O(n) time without using any division operation right
        
        prefix and suffix array
        let's look at what the prefix array would look like
        [1, 2, 6, 24]
        [ 24, 24,12,4]
        
        so when i don't use a number the result is just the prefix before that
        number time the suffix after that number because those totaly isolate the number
        
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
        '''
        
    # so ya this works but can u optimise the space
    # so here is the approach for the prefix and also the suffix array 
    # i can just do them inplace with out using any extra space right
    
    '''
    nums = [1, 2, 3, 4]
    nums = [1, 2, 6, 24]
    
    and for the answer part while going through nums from the right
    and get the prefix and also compute the suffix their and give the res
                    
    '''
    