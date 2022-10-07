class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        stack = []
        last = None
        
        for idx in range(len(nums)-1, -1, -1):
            while stack and nums[stack[-1]] > nums[idx]:
                last = stack.pop()
            
            if last:
                nums[idx], nums[last] = nums[last], nums[idx]
                break
            stack.append(idx)
        
        if not last:
            return -1
        
        nums = nums[:idx+1] + nums[idx+1:][::-1]
        res = int("".join(nums)) 
        
        return res if res <= 2**31-1 else -1
            
        
        