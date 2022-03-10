class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpro = 0
        l, h = 0, 1
        
        while h < len(prices):
            if prices[h] > prices[l]:
                maxpro += (prices[h]-prices[l])
                l = h
            else:
                l = h
            h += 1
        return maxpro
                
        
    