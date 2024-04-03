class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # there is just one to one mapping
        if len(s) != len(t): return False
        
        check1 = check2 = True
        char_map = {}
        char_map2 = {}
        
        for idx in range(len(s)):
            if s[idx] not in char_map:
                char_map[s[idx]] = t[idx]
                
            if char_map[s[idx]] != t[idx]:
                check1 = False
                
            if t[idx] not in char_map2:
                char_map2[t[idx]] = s[idx]
                
            if char_map2[t[idx]] != s[idx]:
                check2 = False
            
            char_map[s[idx]] = t[idx]
            char_map2[t[idx]] = s[idx]
        
        return check1 and check2
            