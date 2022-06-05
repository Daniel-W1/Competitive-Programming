class Solution:
    def thousandSeparator(self, n: int) -> str:
        new = []
        prev = len(str(n))-1
        for i in range(len(str(n))-1,-1,-1):
            new.append(str(n)[i])
            if i == prev-2 and i > 0:
                new.append(".")
                prev = i-1
            i -= 1
        return "".join(new[::-1])
            
            