class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        
        stack = []
        for val in num:
            while k > 0 and stack and stack[-1] > val:
                k -= 1
                stack.pop()
            stack.append(val)
            
        stack = stack[:len(stack)-k]
        res = "".join(stack)
        
        return str(int(res)) if res else "0"
            
                        
                        
        
        