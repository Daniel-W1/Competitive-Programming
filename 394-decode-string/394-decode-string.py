# class Solution:
#     def decodeString(self, s: str) -> str:
#         stack = []
#         ans = []
#         for letter in s:
#             if letter != "]":
#                 stack.append(letter)
#             else:
#                 temp = []
#                 while stack[-1] != "[":
#                     temp.append(stack.pop())
#                 stack.pop()
#                 if stack: 
#                     num = ""
#                     while stack and stack[-1].isnumeric():
#                         num += (stack.pop())
#                     num = int(num[::-1])
#                     temp = temp*num
#                 stack += temp[::-1]
                
#         return "".join(stack)
                    
class Solution:
    def decodeString(self, s: str) -> str:
        self.s = s
        self.pos = 0
        return ''.join(self.decode_level())
            
    def peek(self):
        try:
            return self.s[self.pos]
        except IndexError:
            return
        
    def next(self):
        char = self.peek()
        if char:
            self.pos += 1
            return char

    def decode_level(self):
        res = []
        char = self.next()
        while char:
            if char.isalpha():
                res.append(char)
            elif char.isnumeric():
                num_str = char
                while self.peek().isnumeric():
                    num_str += self.next()
                assert self.next() == '['
                child_result = self.decode_level()
                res.extend(int(num_str) * child_result)
            elif char == ']':
                break
            char = self.next()
        return res
                    
                    
            
                
            
            
            
            