class Solution:
    def jump(self, nums: List[int]) -> int:
        i = len(nums)-1
        cnt = 0
        while i > 0:
            min_ind = i
            for ind in range(i, -1, -1):
                if ind + nums[ind] >= i:
                    min_ind = min(min_ind, ind)
            i = min_ind
            cnt += 1
        return cnt
            
                
            
                
            
            
            
        