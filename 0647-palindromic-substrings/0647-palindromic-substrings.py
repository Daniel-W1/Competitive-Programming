class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l,h = i,i
            while l >= 0 and h < len(s) and s[l]==s[h]:
                res += 1
                l -= 1
                h += 1
            l,h = i,i+1
            while l >= 0 and h < len(s) and s[l]==s[h]:
                res += 1
                l -= 1
                h += 1
        return res
        
        