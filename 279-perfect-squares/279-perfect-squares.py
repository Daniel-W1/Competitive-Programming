class Solution:
    def numSquares(self, n: int) -> int:
        choices = [val**2 for val in range(int(n**0.5)+1,0,-1)]
        def findmin(coins, amount):
                cnt, prev = 0, 1 << amount
                while prev & 1 == 0:
                    curr = prev
                    for coin in coins:
                        curr |= prev >> coin
                    if curr == prev:
                        return -1
                    cnt += 1
                    prev = curr
                return cnt
        res = findmin(choices, n)
        return res
            