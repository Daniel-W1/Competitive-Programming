class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        
        [ -1, 1, 2, 4,5, 7, 12, 14], k = 5, x = 15
            |            |
                 
        deque = [-1, 1, 2, 4, 5]
        
        
        1, 2, 3, 12, 15, 15, k = 4, x = 3
        '''
        insert_pos = bisect_left(arr, x)
        
        # edge cases 
        if insert_pos == 0: return arr[:k]
        if insert_pos == len(arr): return arr[-k:]
        
        left, right = insert_pos - 1, insert_pos 
        ans = deque([])
        
        while left >= 0 and right < len(arr):
            num1 = arr[left]
            num2 = arr[right]
            
            dist1 = abs(x - num1)
            dist2 = abs(x - num2)
            
            if len(ans) == k: break
            
            if dist1 <= dist2:
                ans.appendleft(num1)
                left -= 1
            else:
                ans.append(num2)
                right += 1
        
        while len(ans) < k:
            if left >= 0:
                ans.appendleft(arr[left])
                left -= 1
            elif right < len(arr):
                ans.append(arr[right])
                right += 1
        
        # print(len(ans))
        return ans
        
        