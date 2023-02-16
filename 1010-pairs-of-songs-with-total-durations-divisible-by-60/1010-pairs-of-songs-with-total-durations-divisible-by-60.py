class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        
        cnt = Counter()
        ans = 0
        
        for val in time:
            ans += cnt[60 - val%60] if val%60 else cnt[0]
            cnt[val%60] += 1
        
        return ans