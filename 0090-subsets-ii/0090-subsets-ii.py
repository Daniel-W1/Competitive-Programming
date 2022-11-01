class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
                    1
                1,2   1
             
        '''
        total = []
        path = []
        nums.sort()
        
        def dfs(idx):
            if idx >= len(nums):
                total.append(list(path))
                return
            
            path.append(nums[idx])
            dfs(idx+1)
            path.pop()
            newidx = bisect_left(nums, nums[idx]+1)
            dfs(newidx)
            
        dfs(0)
        return total