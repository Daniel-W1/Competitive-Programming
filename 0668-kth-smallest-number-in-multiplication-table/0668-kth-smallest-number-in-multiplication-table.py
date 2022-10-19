class Solution:
    def count(self, num, n, m):
        cnt = 0
        for row in range(1, n+1):
             cnt += min(num//row, m)
        
        return cnt
            
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left, right = 0, m*n
        ans = -1
        while left <= right:
            mid = (left + right)//2
            
            cnt = self.count(mid, n, m)
            if cnt >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
                
                
            
        
        