class Solution:
    def calculate(self, s: str) -> int:
        
        # keep track of the previous sign
        # when ever u hit some stop put the cur_num with prev sign
        
        
        def calculate(idx):
            def update(sign, num):
                
                if sign == "+": stack.append(num)
                else: stack.append(-num)
                
            
            sign = "+"
            num = 0
            stack = []
            
            while idx < len(s):
                if s[idx].isnumeric():
                    num = num * 10 + int(s[idx])
                
                elif s[idx] in "+-":
                    update(sign, num)
                    sign = s[idx]
                    num = 0
                
                elif s[idx] == "(":
                    
                    num, new_idx = calculate(idx + 1)
                    idx = new_idx - 1
                
                elif s[idx] == ")":
                    update(sign, num)
                    
                    return sum(stack), idx + 1
            
                idx += 1
            
            update(sign, num)
            
            return sum(stack)
    
        return calculate(0)
                
                