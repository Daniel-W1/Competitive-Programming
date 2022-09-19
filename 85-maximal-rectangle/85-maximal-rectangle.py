class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # first let's go through the whole thing and build our
        # dp matrix
        for col in range(len(matrix[0])):
            for row in range(1, len(matrix)):
                if matrix[row][col] != "0":
                    matrix[row][col] =str(int(matrix[row-1][col]) + 1)
        def find(heights):
            stack, ans = [], 0
            for i, h in enumerate(heights + [0]):
                while stack and heights[stack[-1]] >= h:
                    H = heights[stack.pop()]
                    W = i if not stack else i-stack[-1]-1
                    ans = max(ans, H*W)
                stack.append(i)
            return ans
        
        ans = 0
        for row in matrix:
            row = [int(val) for val in row]
            ans = max(ans, find(row))
        
        return ans