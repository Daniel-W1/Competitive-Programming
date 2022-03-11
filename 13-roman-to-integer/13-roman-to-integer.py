class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I" : 1,"V":5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
        num = 0
        l = 0
        while l < len(s):
            if s[l] == "I" and l + 1 < len(s) and s[l+1] in "VX":
                num += (romans[s[l+1]] - romans[s[l]])
                l += 2
            elif s[l] == "X" and l + 1 < len(s) and s[l+1] in "LC":
                num += (romans[s[l+1]] - romans[s[l]])
                l += 2
            elif s[l] == "C" and l + 1 < len(s) and s[l+1] in "DM":
                num += (romans[s[l+1]] - romans[s[l]])
                l += 2
            else:
                num += romans[s[l]]
                l += 1
        return num