class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        
        for idx, val in enumerate(height):
            while stack and val >= height[stack[-1]]:
                mid_height = stack.pop()
                if stack:
                    max_water_height = min(height[stack[-1]], val) - height[mid_height]
                    width = idx - stack[-1] - 1
                    ans += width *  max_water_height
            
            stack.append(idx)
        
        return ans