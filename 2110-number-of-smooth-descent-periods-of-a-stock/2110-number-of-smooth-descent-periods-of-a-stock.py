class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        #[-1, -1, -1, 1]
        #[8,6,7,7]
        #[3,2,1,5,4,3,7,6,1,1,1]
        ranges = []
        l, h = 0,1
        p = len(prices)
        others = []
        while h < len(prices):
            prev = prices[l]
            while h < len(prices) and prev-prices[h] == 1:
                prev = prices[h]
                h += 1
            others.append(h-l)
            l = h
            h += 1
        for val in others:
            p += (val**2 -((val-1)/2 + (val-1)**2/2))-val
        return int(p)