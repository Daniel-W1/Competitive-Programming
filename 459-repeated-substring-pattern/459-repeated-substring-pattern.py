class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        '''
        b ab ab a
        
        ba ba ba
        
        4 2 1
        
        so the appraoch is to generate all the factors of the len(s)
        '''
        new = (s + s)[1:-1]
        return new.find(s) != -1