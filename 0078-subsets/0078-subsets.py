class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        total = []
        path = []
        def dfs(idx):
            if idx >= len(nums):
                total.append(list(path))
                return
            path.append(nums[idx])
            dfs(idx+1)
            path.pop()
            dfs(idx+1)
        dfs(0)
        return total
            
            