class Solution:
    def calculate(self, s: str) -> int:
        
        "1 - 2"
        n = len(s)
        
        
        
        def calculate(idx):
            
            def update(sign, num):
                if sign == "+": stack.append(num)
                elif sign == "-": stack.append(-num)
                elif sign == "*": stack.append(int(stack.pop() * num))
                else: stack.append(int(stack.pop()/num))

            num = 0
            sign = "+"
            stack = []
            
            while idx < n:
                
                # print(stack)
                
                if s[idx].isdigit():
                    num = num * 10 + int(s[idx])
                
                elif s[idx] in "+-*/":
                    update(sign, num)
                    sign = s[idx]
                    num = 0
                
                elif s[idx] == "(":
                    num, n_idx = calculate(idx+1)
                    idx = n_idx - 1
                
                elif s[idx] == ")":
                    update(sign, num)
                    return sum(stack), idx+1
                
                idx += 1
            
            update(sign, num)
            
            # print(stack)
            return sum(stack)
                
            
        return calculate(0)