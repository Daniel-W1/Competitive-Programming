class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        """
            acfgbd
            
            1,2,1,2,3, 4  
        """
        prev_chars = [0] * 26
        dp = [0] * len(s)
        
        for idx, char in enumerate(s):
            pos_idx = ord(char) - 97
            for p_idx, val in enumerate(prev_chars):
                if pos_idx - k <= p_idx <= pos_idx + k:
                    dp[idx] = max(dp[idx], prev_chars[p_idx] + 1)
            
            prev_chars[pos_idx] = dp[idx]
        
        return max(dp)