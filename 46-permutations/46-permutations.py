class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        path = []
        def dfs(nums):
            if not nums:
                ans.append(list(path))
                
            n = len(nums)
            for idx in range(n):
                cur = nums.pop(idx)
                path.append(cur)
                dfs(nums)
                nums.insert(idx, cur)
                path.pop()
        
        dfs(nums)
        return ans