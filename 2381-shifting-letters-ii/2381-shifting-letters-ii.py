class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0]*len(s)
        for left, right, direction in shifts:
            prefix[left] += 1 if direction else -1
            if right + 1 < len(s):
                prefix[right+1] -= 1 if direction else -1
        
        
        prefix = list(accumulate(prefix))
        new = ""
        
        '''
        122 + 25
        '''
        for idx, val in enumerate(prefix):
            new_code = (((ord(s[idx]) + val) - 97) % 26) + 97
            new += chr(new_code)
            
        return new