class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
            [1, 2, 3, 4]
            
            [4, 3, 2, 1]
        
        """
        n, m = len(matrix), len(matrix[0])
        ans = 0
        
        for r in range(n):
            for c in range(m):
                matrix[r][c] = int(matrix[r][c])
                if r and matrix[r][c]:
                    matrix[r][c] += matrix[r-1][c]
            
            
            stack = []
            
            for idx, val in enumerate(matrix[r] + [0]):
                while stack and matrix[r][stack[-1]] >= val:
                    popped_idx = stack.pop()
                    width = idx - stack[-1] - 1 if stack else idx
                    ans = max(ans, width*matrix[r][popped_idx])
                
                stack.append(idx)
            
        return ans
                    
                    