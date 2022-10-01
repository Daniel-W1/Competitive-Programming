class Solution:
    def numDecodings(self, s: str) -> int:
        
        '''
        226
        [1, 2, 3]
        
        1111
        [1, 2, 3,]
        
        at each index their are choices i need to make for example 
        if the cur num is 1 we definetly have two choices 
        
        if the cur is 2 and the next is <= 6 we will have two choices
        
        else we only have on choices
        
        
        that makes sense but how are u going to handle the 0s
        
        if we find a zero we will look at the value we get before 0 and 
        if that value with 0 gives us a valid thing then the whole thing 
        must be valid
        
        my state is one and time comp 2^n am making 2 decision at each index
        O(N)
        
        '''
        @cache
        def dfs(idx):
            if idx >= len(s): return 1
            
            if s[idx] == "1" and idx + 1 < len(s):
                return dfs(idx + 1) + dfs(idx + 2)
            
            elif s[idx] == "2" and idx + 1 < len(s) and int(s[idx+1]) <= 6:
                return dfs(idx + 1) + dfs(idx + 2)
        
            elif int(s[idx]) >= 1:
                return dfs(idx+1)
            else:
                return 0
        return dfs(0)
            
                