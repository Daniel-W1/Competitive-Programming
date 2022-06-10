class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = (0,0)
        reslen = 0
        
        for i in range(len(s)):
            # let's try to do this for odds first.
            l, h = i,i
            while l >= 0 and h < len(s) and s[l] == s[h]:
                if (h-l+1) > reslen:
                    reslen = h-l+1
                    res = (l,h+1)
                l -= 1
                h += 1
            # let's do the same thing for the even ones
            
            l,h = i, i+1
            while l >=0  and h < len(s) and s[l] == s[h]:
                if (h-l+1) > reslen:
                    reslen = h-l+1
                    res = (l,h+1)
                l -= 1
                h += 1
        return s[res[0]:res[1]]
            
            
            
            
       
                    
                    
        
        
            
                
            
                
                
        
        