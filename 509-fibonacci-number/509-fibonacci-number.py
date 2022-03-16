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
            