class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for num in popped:
            if stack and stack[-1] == num:
                stack.pop()
            elif i < len(pushed):
                while i < len(pushed) and pushed[i] != num:
                    stack.append(pushed[i])
                    i += 1
                i += 1
            else:
                return False
        return True
    
        