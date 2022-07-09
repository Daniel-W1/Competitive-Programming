class Solution:
    def numSub(self, s: str) -> int:
        l = 0
        ans = 0
        formula = lambda val : val/2 *(1+val)
        while l < len(s):
            if s[l] == "1":
                r = l
                while r < len(s) and s[r] == "1":
                    r += 1
                ans += formula(r-l)
                l = r
            l += 1
        return int(ans)%(10**9+7)
                