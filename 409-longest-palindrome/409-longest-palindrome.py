class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        oneOdd = True
        for key in cnt:
            if not cnt[key]%2:
                ans += cnt[key]
            elif oneOdd:
                ans += cnt[key]
                oneOdd = False
            else:
                ans += cnt[key]-1
        return ans
                
                