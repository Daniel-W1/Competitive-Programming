class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        return (pow(2**p -2, 2**(p-1) - 1, 10**9 + 7) * (2**p - 1)) % (10**9 + 7)