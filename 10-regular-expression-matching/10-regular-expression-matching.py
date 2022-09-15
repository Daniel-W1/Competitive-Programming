class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def check(idx1, idx2):
            basecase1 = idx1 == len(s)
            basecase2 = idx2 == len(p)
            
            if basecase1 and basecase2: return True
        
            curchar = s[idx1] if idx1 < len(s) else ""
            curpchar = p[idx2] if idx2 < len(p) else ""
            nextpchar = p[idx2+1] if idx2+1 < len(p) else None
            
            if (basecase1 or basecase2) and not nextpchar: return False
            
            if (curchar == curpchar or curpchar == ".") and nextpchar != "*":
                return check(idx1+1, idx2+1)
            
            elif (curchar == curpchar or curpchar == ".") and nextpchar == "*":
                if curpchar == ".": 
                    curchar = s[idx1] if idx1 < len(s) else ""
                while idx1 < len(s) and s[idx1] == curchar:
                    res = check(idx1, idx2+2)
                    if res: return True
                    idx1 += 1
                    if idx1 < len(s) and curpchar == ".":
                        curchar = s[idx1]
                    
                return check(idx1, idx2+2)
            elif nextpchar == "*":
                return check(idx1, idx2+2)
            else:
                return False
        return check(0,0)
                