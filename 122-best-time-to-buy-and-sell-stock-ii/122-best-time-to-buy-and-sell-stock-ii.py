class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpro = 0
        l = 0
        
        for h in range(1, len(prices)):
            if prices[h] > prices[l]:
                maxpro += (prices[h]-prices[l])
                l = h
            else:
                l = h

        return maxpro
                
        
    