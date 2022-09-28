class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        left, right = 0, 0
        
        while right < len(prices):
            maxprofit = max(maxprofit, prices[right] - prices[left])
            
            if prices[right] < prices[left]:
                left = right
            
            right += 1
        
        return maxprofit
        
        