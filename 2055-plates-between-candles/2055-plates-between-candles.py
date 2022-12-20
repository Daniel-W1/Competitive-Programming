class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix = [0]
        candles = []
        
        for idx, char in enumerate(s):
            if char == "*":
                prefix.append(prefix[-1] + 1)
            else:
                candles.append(idx)
                prefix.append(prefix[-1])
        
        ans = []
        # print(candles)
        # print(prefix)
        
        for l, h in queries:
            idx = bisect_left(candles, l)
            idx2 = bisect_right(candles, h) - 1
            
            if candles and idx2 > idx:
                ans.append(max(0, prefix[candles[idx2]] - prefix[candles[idx]]))
            else:
                ans.append(0)
        
        return ans