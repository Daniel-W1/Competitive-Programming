from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        
        digits = deque(digits)
        i = len(digits)-1
        carry = digits[i]+1//10
        while carry and i >= 0:
            carry = (digits[i]+1)//10
            digits[i] = (digits[i]+1)%10
            i -= 1
        if carry:
            digits.appendleft(carry)
        return digits
            
        
            
            