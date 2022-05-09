class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ranges = []
        l, h = 0,1
        p = len(prices)
        others = []
        while h < len(prices):
            prev = prices[l]
            while h < len(prices) and prev-prices[h] == 1:
                prev = prices[h]
                h += 1
            val = h-l
            p += (val**2 -((val-1)/2 + (val-1)**2/2))-val
            l = h
            h += 1
        return int(p)