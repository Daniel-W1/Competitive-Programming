class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        new_n = abs(n)
        if new_n%2 == 0:
            simple = self.myPow(x, new_n//2)
            ans = simple*simple
            return ans if n >= 0 else 1/(ans)
        else:
            simple = self.myPow(x, new_n//2)
            ans = x * simple * simple
            return ans if n >= 0 else 1/(ans)
        
        
            