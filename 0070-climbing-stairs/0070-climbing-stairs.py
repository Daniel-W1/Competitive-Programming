class Solution:
    def climbStairs(self, n: int) -> int:
        
        fib1, fib2 = 1, 1
        cur = 0
        
        for stair in range(2, n+1):
            cur = fib1 + fib2
            fib1, fib2 = fib2, cur
        
        return fib2
        