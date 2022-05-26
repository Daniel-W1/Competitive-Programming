class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            if n%2 == 1:
                cnt += 1
            n //= 2
        return cnt
            
            