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
        
        res = factors(len(s))
        # print(res)
        for num in res:
            check = True
            prev = s[:num]
            cur = s[num]
            for idx in range(num+1, len(s)):
                if not idx%num:
                    if cur != prev:
                        check = False
                        break
                    cur = ""
                cur += s[idx]
            if cur != prev:
                check = False
    
            # print(check)
            if check:
                return True
        return False
                
        
                             