class Solution:
    def numberOfWays(self, s: str) -> int:
        """
            here are the states
            
            how many building have u selected
            the previous building
        """
        n = len(s)
        cnt = [0]*n
        zero_cnt, one_cnt = 0, 0
        
        for idx, char in enumerate(s):
            if not int(s[idx]):
                cnt[idx] = one_cnt
                zero_cnt += 1
            else:
                cnt[idx] = zero_cnt
                one_cnt += 1
            
        
        zero_cnt, one_cnt = 0, 0
        ans = 0
        for idx in range(n-1, -1, -1):
            if not int(s[idx]):
                ans += (cnt[idx] * one_cnt)
                zero_cnt += 1
            else:
                ans += (cnt[idx] * zero_cnt)
                one_cnt += 1
            
        return ans
        
        