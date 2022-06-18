class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispali(l,h,word):
            l,h = 0,len(word)-1
            while l < h:
                if word[l] != word[h]:
                    return False
                l += 1
                h -= 1
            return True
        l,h = 0,len(s)-1
        while l < h:
            if s[l] != s[h]:
                word1 = s[:h] + s[h+1:]
                word2 = s[:l] + s[l+1:]
                check1 = ispali(l,h,word1)
                check2 = ispali(l,h,word2)
                return check1 or check2
            l += 1
            h -= 1
        return True