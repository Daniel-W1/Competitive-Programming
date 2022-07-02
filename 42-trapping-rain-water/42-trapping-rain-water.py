class Solution:
    def trap(self, height: List[int]) -> int:
#         minStack = []
#         l = 0
#         water = 0
#         while l < len(height) and height[l] == 0:
#             l += 1
#         for h in range(l,len(height)):
#             while minStack and height[minStack[-1]] < height[h]:
#                 hole = minStack.pop()
#                 dist = h - minStack[-1] - 1 if minStack else 0
#                 left = minStack[-1] if minStack else hole
#                 water += (min(height[left],height[h])-height[hole])*dist
#             minStack.append(h)
#         return water
        left = 0
        right = len(height)-1
        
        max_left = height[0]
        max_right = height[-1]
        cur = left
        water = 0
        while left < right:
            max_left = max(max_left,height[left])
            max_right = max(max_right,height[right])
            
            if (min(max_left,max_right)-height[cur]) > 0:
                water += (min(max_left,max_right)-height[cur])
            
            if max_left <= max_right:
                left += 1
                cur = left
            else:
                right -= 1
                cur = right
        return water
            