class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1 or n == 4:
            return True
        elif n > 4:
            return self.isPowerOfFour(n/4)
        else:
            return False
