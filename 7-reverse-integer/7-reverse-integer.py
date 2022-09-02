class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)
        reversed_num = 0
        
        while x:
            last_digit = x%10
            reversed_num = reversed_num *10 + last_digit
            x //= 10
        
        if not -2**31 <= reversed_num <= 2**31-1:
            return 0
        return -reversed_num if is_negative else reversed_num