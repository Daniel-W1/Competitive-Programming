class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        psum = [0]*n
        s = [char for char in s]
        
        for start,end,direction in shifts:
            shift = 1 if direction == 1 else -1
            psum[start]+=shift
            if end+1<n: psum[end+1]-=shift
        
        for i in range(1,n):
            psum[i] = psum[i-1] + psum[i]
        
        for i in range(n):
            new_char = chr((((ord(s[i]) + psum[i]) - 97) % 26) + 97)
            s[i] = new_char
        
        return "".join(s)