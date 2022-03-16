class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            if n == 2: return 1
            return n
        else:
            ans = [0]*(n+1)
            ans[0], ans[1], ans[2] = 0,1,1
            for i in range(3, len(ans)):
                ans[i] = ans[i-3]+ans[i-2]+ans[i-1]
            return ans[-1]