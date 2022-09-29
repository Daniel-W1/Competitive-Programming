class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # first let's check if the element have a next smaller element
        next_smaller = {idx : False for idx in range(len(arr))}
        stack = []
        for idx in range(len(arr)):
            while stack and arr[stack[-1]] > arr[idx]:
                next_smaller[stack.pop()] = True
            stack.append(idx)
        
        minElement = [0]*len(arr)
        minElement[-1] = arr[-1]
        for idx in range(len(arr)-2, -1, -1):
            minElement[idx] = min(arr[idx], minElement[idx+1])
        # print(len(stack))
        # print(next_smaller)
        # print(minElement)
        seen_max = -1
        ans = 0
        for idx in range(len(arr)):
            seen_max = max(seen_max, arr[idx])
            if not next_smaller[idx] and idx + 1 < len(arr) and seen_max < minElement[idx+1]:
                ans += 1
                
        return ans + 1