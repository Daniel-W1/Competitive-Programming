class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        def bs(cur):
            # print(stack)
            left, right = 0, len(stack)-1
            while left <= right:
                mid = (left + right)//2
                if nums[stack[mid]] == cur:
                    return stack[mid]
                elif nums[stack[mid]] > cur:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            res = stack[left]
            return res if nums[stack[left]] < cur else res + 1
            
        max_size = 0
        for idx, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(idx)
            else:
                res = bs(num)
                # print(idx, res, num, stack)
                max_size = max(max_size, idx - res)
            # print(max_size)
        return max_size
                