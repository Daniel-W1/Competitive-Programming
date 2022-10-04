class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        coins.sort(reverse = True)
        
        @cache
        def dfs(start, target):
            if target <= 0:
                return int(target == 0)
            
            res = 0
            for idx in range(start, len(coins)):
                coin = coins[idx]
                res += dfs(idx, target - coin)
                
            return res
        
        return dfs(0, amount)