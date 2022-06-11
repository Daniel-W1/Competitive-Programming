class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        prefix = [0]*len(nums)
        postfix = [0]*len(nums)
        prev1,prev2 = 0, 0
        last = len(nums)-1
        
        for i in range(len(nums)):
            prefix[i] = prev1 + nums[i]
            postfix[last] = prev2 + nums[last]
            prev1,prev2 = prefix[i],postfix[last]
            last -= 1
        
        post_map = {}
        for i in range(len(postfix)):
            post_map[postfix[i]] = len(postfix)-i
        l,h = 0,len(nums)-1
        ans = float('inf')
        while l < len(nums) and prefix[l] < x:
            l += 1
        if l < len(nums) and prefix[l] == x:
            ans = min(ans,l+1)
        while h >= 0 and postfix[h] < x:
            h -= 1
        if h >= 0 and postfix[h] == x:
            ans = min(ans,len(prefix)-h)
        for i in range(len(prefix)):
            target = x-prefix[i]
            if target in post_map and len(nums)-post_map[target] > i:
                ans = min(ans,post_map[target]+i+1)
        return ans if ans < float('inf') else -1