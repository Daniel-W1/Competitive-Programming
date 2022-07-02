class Solution:
    def trap(self, height: List[int]) -> int:
        minStack = []
        l = 0
        water = 0
        while l < len(height) and height[l] == 0:
            l += 1
        for h in range(l,len(height)):
            while minStack and height[minStack[-1]] < height[h]:
                hole = minStack.pop()
                dist = h - minStack[-1] - 1 if minStack else 0
                left = minStack[-1] if minStack else hole
                water += (min(height[left],height[h])-height[hole])*dist
                
            minStack.append(h)
        return water
            