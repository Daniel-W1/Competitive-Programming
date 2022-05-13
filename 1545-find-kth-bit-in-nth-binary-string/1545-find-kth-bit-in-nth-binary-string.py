class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(string):
            newstring = ''
            for n in string:
                if n == "0":
                    newstring += "1"
                else:
                    newstring += "0"
            return newstring
        memo = {}      
        def recur(n):
            if n == 1:
                return "0"
            if n not in memo:
                memo[n] = recur(n-1) + "1" + invert(recur(n-1))[::-1]
            return memo[n]
        return recur(n)[k-1]
            