class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # first let's check if the element have a next smaller element
        next_smaller = {idx : False for idx in range(len(arr))}
        stack = []
        for idx in range(len(arr)):
            while stack and arr[stack[-1]] > arr[idx]:
                next_smaller[stack.pop()] = True
            stack.append(idx)
        
        # print(next_smaller)
        seen_max = -1
        ans = 0
        for idx in range(len(arr)):
            seen_max = max(seen_max, arr[idx])
            if not next_smaller[idx] and idx+1 < len(arr) and seen_max < min(arr[idx+1:]):
                ans += 1
                
                
        return ans + 1