class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        nums.sort()
        
        memo = {}
        def dp(idx, prev_lcm):
            
            if (idx, prev_lcm) in memo: return memo[idx, prev_lcm]
            if idx == n:
                return 0
            
            cur_lcm = lcm(prev_lcm, nums[idx])
            res = 0
            
            if cur_lcm == prev_lcm or cur_lcm == nums[idx]:
                res = max(res, dp(idx+1, cur_lcm) + 1)
            
            res = max(res, dp(idx + 1, prev_lcm))
            memo[idx, prev_lcm] = res
            
            return res

        
        max_start = -1
        res = -1
        for idx in range(n):
            cur_res = dp(idx, nums[idx])

            if cur_res >= res:
                res = cur_res
                max_start = idx
        
        target = res
        prev_lcm = nums[max_start]
        ans = []
        
        for idx in range(max_start, n):
            cur = lcm(nums[idx], prev_lcm)
            
            if (idx, cur) in memo and memo[idx, cur] == target:
                prev_lcm = cur
                ans.append(nums[idx])
                target -= 1
            
            if not target:
                break
                
        return ans