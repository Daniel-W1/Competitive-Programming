class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        
        memo = {}
        n = len(price)
        
        def dfs(needs):
            if tuple(needs) in memo:
                return memo[tuple(needs)]
            
            val = sum([price[idx]*needs[idx] for idx in range(n)])
            for offer in special:
                new = [needs[idx] - offer[idx] for idx in range(n)]
                if min(new) >= 0:
                    val = min(val, memo.get(tuple(new), dfs(new)) + offer[-1])
            
            memo[tuple(needs)] = val
            
            return val
        
        return dfs(needs)
            
            
            