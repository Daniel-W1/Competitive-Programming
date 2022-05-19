class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def generate(ans, left, right):
            if left and right:
                return generate(ans+"(", left-1, right) and generate(ans+")",left,right-1)
            if left:
                return generate(ans+"(",left-1,right)
            if right:
                return generate(ans+")",left,right-1)
            if not right and not left:
                # i need to check whether the parenthesis combination is valid or not
                stack = []
                check = True
                for item in ans:
                    if item in "(":
                        stack.append(item)
                    else:
                        if stack:
                            stack.pop()
                        else:
                            check = False
                            break
                if check:
                    output.append(ans)
                return output
        
        return generate("",n,n)