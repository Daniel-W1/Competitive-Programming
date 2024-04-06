class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        ans = list(s)
        
        for idx, char in enumerate(s):
            if char == "(":
                stack.append(idx)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    ans[idx] = ""
        
        for idx in stack: ans[idx] = ""
        return "".join(ans)