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
            idx2 = bisect_left(candles, h)
            
            if idx == len(candles):
                idx -= 1
                
            if idx2 == len(candles) or candles[idx2] > h:
                idx2 -= 1
            # print(idx, idx2, "here")
            if candles and idx2 > idx:
                ans.append(max(0, prefix[candles[idx2]] - prefix[candles[idx]]))
            else:
                ans.append(0)
        
        return ans