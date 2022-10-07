class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []
        path = []
        def dfs(idx, target):
            if target == 0:
                ans.append(list(path))
                return
            
            if target < 0:
                return 
            
            for idx in range(idx, len(nums)):
                path.append(nums[idx])
                dfs(idx, target - nums[idx])
                path.pop()
        
        dfs(0, target)
        return ans
        
                