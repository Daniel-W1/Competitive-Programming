class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        string = list(s)
        for val in string:
            if val != ")":
                stack.append(val)
            else:
                temp = []
                
                while stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()
                stack += temp
                
        return "".join(stack)
            
            
        
        