class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        '''
        ab ab ab
        
        ba ba ba
        
        4 2 1
        
        so the appraoch is to generate all the factors of the len(s)
        '''
        if len(s) == 1: return False
        def factors(n):
            ans = []
            for num in range(1, int(sqrt(n)+1)):
                if not n%num:
                    ans.append(num)
                
                    if n//num != num and num != 1:
                        ans.append(n//num)
            
            return ans
        
        res = sorted(factors(len(s)), reverse = True)
        # print(res)
        for num in res:
            check = []
            cur = ""
            for idx in range(len(s)):
                if not idx%num and idx:
                    check.append(cur)
                    cur = ""
                cur += s[idx]
            check.append(cur)
            # print(check)
            if len(set(check)) == 1:
                return True
        return False
                
        
                             