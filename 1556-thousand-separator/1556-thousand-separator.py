class Solution:
    def thousandSeparator(self, n: int) -> str:
        num = str(n)
        new = ""
        i = len(num)-1
        prev = i
        while i >= 0:
            new += num[i]
            if i == prev-2 and i > 0:
                new += "."
                prev = i-1
            i -= 1
        return new[::-1]
            
            