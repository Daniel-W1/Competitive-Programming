class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, h = 0, 1
        ans = 0
        
        while h < len(prices):
            if prices[h] > prices[l]:
                ans = max(ans, prices[h]- prices[l])
            else:
                l = h
            h += 1
            
        return ans