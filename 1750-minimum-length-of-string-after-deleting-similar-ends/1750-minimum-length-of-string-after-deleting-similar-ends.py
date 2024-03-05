class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s)-1
        
        
        while left < right:
            if s[left] == s[right]:
                the_chr = s[left]
                while left < len(s) and s[left] == the_chr:
                    left += 1
                while right >= 0 and s[right] == the_chr:
                    right -= 1
            else:
                break
        
        return max(0, right - left + 1)