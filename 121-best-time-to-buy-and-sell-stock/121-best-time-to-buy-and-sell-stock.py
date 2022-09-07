class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices = [7, 1, 5, 3, 6, 4 ]
        #                          1  
        #                       1
        
        cur_min = prices[0]
        ans = 0
        
        for idx in range(1, len(prices)):
            if prices[idx] < cur_min:
                cur_min = prices[idx]
            else:
                ans = max(ans, prices[idx]-cur_min)
        return ans