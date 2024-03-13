class Solution:
    def pivotInteger(self, n: int) -> int:
        left, right = 1, n
        
        while left <= right:
            mid = (left + right)//2
            
            left_sum = mid * (mid + 1)/2
            right_sum = (mid + n) * (n - mid + 1)/2
                        
            if right_sum == left_sum:
                return mid
            elif right_sum > left_sum:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1