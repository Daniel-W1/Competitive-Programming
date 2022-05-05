class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = {}
        # memo[1] = 1
        # memo[2] = 2
        # def climb(n):
        #     if n in memo:
        #         return memo[n]
        #     else:   
        #         memo[n] =  climb(n-1) + climb(n-2)
        #         return memo[n]
        # return climb(n)
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(2, n):
            tmp = b
            b = a+b
            a = tmp
        return b

            
            