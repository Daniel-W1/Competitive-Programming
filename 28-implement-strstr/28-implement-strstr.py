class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        l = 0
        while l < len(haystack):
            if haystack[l] == needle[0]:
                check = haystack[l:l+len(needle)] == needle
                if check: return l
            l += 1
        return -1