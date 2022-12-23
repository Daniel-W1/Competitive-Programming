class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        @cache
        def dfs(idx, state):
            if idx >= n:
                return 0
            
            if state == -1:
                return max(dfs(idx + 1, prices[idx]), dfs(idx + 1, -1))
            else:
                return max(dfs(idx + 2, -1) + prices[idx] - state, dfs(idx + 1, state))
        
        return dfs(0, -1)