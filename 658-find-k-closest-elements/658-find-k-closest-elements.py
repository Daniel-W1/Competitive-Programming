class Solution:
    def findClosestElements(self, A: List[int], k: int, x: int) -> List[int]:
        '''
        
        [ -1, 1, 2, 4,5, 7, 12, 14], k = 5, x = 15
            |            |
                 
        deque = [-1, 1, 2, 4, 5]
        
        
        1, 2, 3, 12, 15, 15, k = 4, x = 3
        '''
        left, right = 0, len(A) - k
        while left < right:
            mid = (left + right) // 2
            if x - A[mid] > A[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return A[left:left + k]
        