class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+" : add, "-" : sub, "*": mul, "/": truediv}
        
        stack = []
        
        for char in tokens:
            if char not in ops:
                stack.append(char)
            else:
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(ops[char](int(num2), int(num1))))

        return int(stack[0])
                