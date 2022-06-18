class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispali(l,h):
            while l < h:
                if s[l] != s[h]:
                    return False
                l += 1
                h -= 1
            return True
        l,h = 0,len(s)-1
        
        while l < h:
            if s[l] != s[h]:
                check1 = ispali(l+1,h)
                check2 = ispali(l,h-1)
                
                return check1 or check2
            l += 1
            h -= 1
        return True