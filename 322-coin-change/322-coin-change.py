class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [amount+1]*(amount+1)
#         dp[0] = 0
        
#         for a in range(1, amount+1):
#             for c in coins:
#                 if a-c >= 0:
#                     dp[a] = min(dp[a], 1+dp[a-c])
#         return dp[amount] if dp[amount] < amount+1 else -1
    
    # ugly but fast solution 
            cnt, prev = 0, 1 << amount
            while prev & 1 == 0:
                curr = prev
                for coin in coins:
                    curr |= prev >> coin
                if curr == prev:
                    return -1
                cnt += 1
                prev = curr
            return cnt