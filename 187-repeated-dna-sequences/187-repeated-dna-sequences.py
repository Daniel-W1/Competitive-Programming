class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # print(10*(4**9))
        h = {
            'A':1,
            'C':2,
            'G':3,
            'T':4
        }
        
        mod = 10**9 + 7
        mult = 4**9
        ans = []
        found = {}
        
        code = 0
        for i in range(min(10, len(s))):
            code += h[s[i]] * (4**i)
            
        found[code] = 1 
        
        i = 0
        j = 10
        while j < len(s):
            code -= h[s[i]] 
            code //= 4
            
            code += h[s[j]] * mult
            
            i+=1
            j+=1
            
            if code in found:
                if found[code] == 1:
                    ans.append(s[i:j])
                    found[code] +=1
            else:
                found[code] =1
        
        return ans