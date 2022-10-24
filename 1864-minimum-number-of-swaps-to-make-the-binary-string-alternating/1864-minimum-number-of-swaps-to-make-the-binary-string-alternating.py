class Solution:
    def minSwaps(self, s: str) -> int:
        '''
        101010
        010101
        '''
        n = len(s)
        # first let's start from 1
        ans = float('inf')
        ones = 0
        zeros = 0
        
        for idx in range(n):
            if not idx & 1 and s[idx] != "1":
                zeros += 1
            
            if idx & 1 and s[idx] != "0":
                ones += 1
        
        if ones == zeros:
            ans = min(ans, ones)

        
        ones = 0
        zeros = 0
        for idx in range(n):
            if not idx & 1 and s[idx] != "0":
                ones += 1
            
            if idx & 1 and s[idx] != "1":
                zeros += 1
        
        if ones == zeros:
            ans = min(ans, ones)
            
        return ans if ans != float("inf") else -1
        
                
        
            