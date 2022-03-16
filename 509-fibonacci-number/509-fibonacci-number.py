class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            ans = [0]*n
            ans[0]=ans[1]= 1
            for i in range(2, len(ans)):
                ans[i] = ans[i-2]+ans[i-1]
        return ans[-1]
    # the above code is an example of dp and 
    # we can do this problem with naive recursion but that would take a ton of time
    # the time complexity of naive rec and dp is 2^n , O(n) respectively
            