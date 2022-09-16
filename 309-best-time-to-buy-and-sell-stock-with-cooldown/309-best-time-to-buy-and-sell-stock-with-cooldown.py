class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we need to keep track of the idx we are at
        '''
         @cache
        def find(idx, status):
            if idx >= len(prices):
                return 0
            if status == -1: # that means I can buy
                return max(find(idx+1, prices[idx]), find(idx+1, -1))
            elif prices[idx] > status:
                return max(find(idx+2, -1) + prices[idx] - status, find(idx+1, status))
            else:
                return find(idx+1, status)
            
        return find(0, -1)
        
        '''
        '''
          dp = [0]*len(prices)
        for idx in range(len(prices)):
            if idx == 0: dp[0] = 0
            elif idx == 1: dp[idx] = max(0, prices[idx] - prices[0])
            else:
                # atleast we can make the previous amount
                dp[idx] = dp[idx-1]
                for pidx in range(idx-1, -1, -1):
                    max_prev = dp[pidx-2] if pidx - 2 >= 0 else 0
                    dp[idx] = max(dp[idx], max_prev + prices[idx]-prices[pidx])
        return dp[-1]
        # this is the n^2 dp 
        '''
        # here is the best time O(n), space O(n) sol
        # we can drive this sol from the above because 
        # the second loop which is 
        '''
        max_prev + prices[idx] - prices[pidx] part only the prices[pidx] and max_prev are changing all the others are the same 
        
        so we can keep track of the maximum 
        max_prev - prices[idx]
        '''
        max_diff = -float('inf')
        dp = [0]*len(prices)
        
        for idx in range(len(prices)):
            if idx == 0:
                max_diff = max(max_diff, -prices[idx])
                dp[0] = 0
            elif idx == 1:
                max_diff = max(max_diff, -prices[idx])
                dp[idx] = max(0, prices[idx] - prices[0])
            
            else:
                dp[idx] = max(dp[idx-1], max_diff + prices[idx])
                max_diff = max(max_diff,dp[idx-2] - prices[idx])
        
        return dp[-1]
    
        # time O(n), space O(n)
        # Done !!