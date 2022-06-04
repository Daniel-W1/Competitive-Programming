class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
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