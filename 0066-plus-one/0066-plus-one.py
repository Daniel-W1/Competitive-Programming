class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        idx = len(digits)-1
        carry = 1
        
        while idx >= 0:
            cur = digits[idx]
            
            real_cur = cur + carry
            digits[idx] = real_cur%10
            carry = (real_cur)//10
            
            idx -= 1
            
            if not carry: break
        
        return digits if not carry else [carry] + digits
        