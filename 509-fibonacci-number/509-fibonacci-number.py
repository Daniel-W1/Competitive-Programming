class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        if n < 2:
            return n
        if n not in memo:
            memo[n] = self.fib(n-1)+self.fib(n-2)
        return memo[n]
    # the above code is an example of dp and 
    # we can do this problem with naive recursion but that would take a ton of time
    # the time complexity of naive rec and dp is 2^n , O(n) respectively
            