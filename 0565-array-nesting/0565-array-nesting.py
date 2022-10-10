class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        memo = {}
        seen = set()
        
        def dfs(node, seen):
            if node in memo:
                return memo[node]
            
            if node in seen:
                return 0
            
            seen.add(node)
            memo[node] = dfs(nums[node], seen) + 1
            return memo[node]
        
        ans = 0
        for num in nums:
            ans = max(ans, dfs(num, seen))
        
        return ans
            
            