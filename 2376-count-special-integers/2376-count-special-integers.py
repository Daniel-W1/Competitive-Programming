class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        """
            okay that was stupid why don't we try to decrease the state
            
            okay here is an idea why don't we count all the special numbers for each 
            length until we reach n
            
            but how do we know we reached n
            
            haha here comes digit dp, beautiful stuff
        """
        nums = str(n)
        # so here are the states, idx, tight boolean, 
        
        @cache
        def dfs(idx, tight, mask):
            if idx == len(nums): 
                return 1
            
            max_range = int(nums[idx]) + 1 if tight else 10
            cur = 0
            
            for num in range(max_range):
                
                # check if the number is repeated
                if 1 << num & mask: continue
                
                if not num and not mask:
                    cur += dfs(idx + 1, False , mask) 
                else:
                    cur += dfs(idx + 1,tight and num==int(nums[idx]),mask | 1 << num) 
                    
            return cur
        
        return dfs(0, True, 0) - 1
        
        