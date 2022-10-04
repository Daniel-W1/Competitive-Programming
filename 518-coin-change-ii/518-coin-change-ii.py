class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        coins.sort(reverse = True)
        @cache
        def dfs(left, target):
            if target <= 0:
                return int(target == 0)
            
            res = 0
            for idx in range(left, len(coins)):
                coin = coins[idx]
                res += dfs(left, target - coin)
                left += 1
                
            return res
        
        return dfs(0, amount)