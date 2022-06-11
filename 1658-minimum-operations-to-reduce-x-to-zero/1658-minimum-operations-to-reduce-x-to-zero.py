class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        prefix = [0]*len(nums)
        postfix = [0]*len(nums)
        prev1,prev2 = 0, 0
        last = len(nums)-1
        ans = float('inf')
        post_map = {}
        
        for i in range(len(nums)):
            prefix[i] = prev1 + nums[i]
            postfix[last] = prev2 + nums[last]
            if prefix[i]== x: 
                ans = min(ans,i+1)
            if postfix[last] == x:
                ans = min(ans, len(nums)-last)
            post_map[postfix[last]] = len(nums)-last
            prev1,prev2 = prefix[i],postfix[last]
            last -= 1
            
        for i in range(len(prefix)):
            target = x-prefix[i]
            if target in post_map and len(nums)-post_map[target] > i:
                ans = min(ans,post_map[target]+i+1)
        return ans if ans < float('inf') else -1