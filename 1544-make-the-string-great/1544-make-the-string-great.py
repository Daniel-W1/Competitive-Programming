class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        is_bad = lambda char1, char2: ord(char1) != ord(char2) and char1.lower() == char2.lower()
        
        for char in s:
            if stack and is_bad(stack[-1], char):
                stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)