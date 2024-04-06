class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        
        for idx, char in enumerate(s):
            if char == "(":
                stack.append(idx)
            elif char == ")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(idx)
        
        stack = set(stack)
        ans = []
        
        for idx, char in enumerate(s):
            if idx not in stack:
                ans.append(char)
        
        return "".join(ans)