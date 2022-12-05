class Solution:
    def countTexts(self, pressedKeys: str) -> int:        
        mod = 10**9 + 7
        n = len(pressedKeys)
        
        dp = [0]*n
        dp[-1] = 1
        
        for idx in range(n-2, -1, -1):
            max_len = 3 if pressedKeys[idx] not in ["7", "9"] else 4
            right = idx
            
            for change in range(1, max_len + 1):
                
                if idx + change < n:
                    dp[idx] += dp[idx + change] 
                else:
                    dp[idx] += 1
                
                dp[idx] %= mod
                if idx + change < n and pressedKeys[idx + change] != pressedKeys[idx] or (idx + change == n):
                    break
                
                
        return dp[0]
    
    
    
    