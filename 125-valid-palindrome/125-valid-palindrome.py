class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        h = len(s)-1
        s = s.lower()
        while l < h:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[h].isalnum():
                h -= 1
                continue
            if s[l] == s[h]:
                l += 1
                h -= 1
            else:
                return False
            
        return True
            
                
                