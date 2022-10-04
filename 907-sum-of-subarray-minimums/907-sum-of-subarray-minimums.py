class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        '''
        so this is a good monostack problem and here is how am going to do it
        first find the next and the prev smaller elements
        
        [4, 3, 1, 2, 4]
        right = {0:1, 1:2, 2:-1, 3:-1, 4:-1}
        left =  {0:-1, 1:-1, 2:-1,3:2, 4:3}
        
        4*1 + 6 + 9 + 4 + 4  = 27
        
        '''
        next_smaller = {idx: -1 for idx in range(len(arr))}
        prev_smaller = {idx : -1 for idx in range(len(arr))}
        
        stack = []
        for idx in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[idx]:
                next_smaller[stack.pop()] = idx
            stack.append(idx)
                
        stack = []
        for idx in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]] > arr[idx]:
                prev_smaller[stack.pop()] = idx
            stack.append(idx)
            
        n = len(arr)
        ans = 0
        # print(next_smaller)
        # print(prev_smaller)
        
        for idx in next_smaller:
            left = idx - prev_smaller[idx] - 1
            end_point = n if next_smaller[idx] == -1 else next_smaller[idx]
            right = end_point - idx
            
            # print(left, right, arr[idx])
            ans += (left*right + right)*arr[idx]
        
        return ans % (10**9 + 7)
            