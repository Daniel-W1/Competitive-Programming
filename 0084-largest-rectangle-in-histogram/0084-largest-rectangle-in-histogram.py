class Solution:
    def largestRectangleArea(self, height):
        height = [0] + height + [0]
        n = len(height)
        answer = 0
        stack = []
        
        for idx in range(n):
            while stack and height[stack[-1]] > height[idx]:
                cur = stack.pop()
                answer = max(answer, height[cur] * (idx - stack[-1]- 1))
            stack.append(idx)
        return answer
                
                
        

    
