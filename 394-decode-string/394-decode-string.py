class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = []
        for letter in s:
            if letter != "]":
                stack.append(letter)
            else:
                temp = []
                while stack[-1] != "[":
                    temp.append(stack.pop())
                stack.pop()
                if stack: 
                    num = ""
                    while stack and stack[-1].isnumeric():
                        num += (stack.pop())
                    num = int(num[::-1])
                    temp = temp*num
                stack += temp[::-1]
                
        return "".join(stack)
                    
                    
            
                
            
            
            
            