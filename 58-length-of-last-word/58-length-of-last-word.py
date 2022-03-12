class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        h = len(s)-1
        length = 0
        while  h >= 0 and s[h] == " ":
            h -= 1
        while h >= 0 and s[h] != " ":
            h -= 1
            length += 1
        return length
            
                
            