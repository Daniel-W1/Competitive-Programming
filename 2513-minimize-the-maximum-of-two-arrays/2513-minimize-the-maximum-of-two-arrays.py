class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, u1: int, u2: int) -> int:
        
        total = u1 + u2
        
        left, right = 0, 10**20
        ans = -1
        
        while left <= right:
            
            mid = (right + left)//2
            
            divisible_1, divisible_2 = mid // divisor1, mid // divisor2
            divisible_by_both = mid // lcm(divisor1, divisor2)
            
            cur_res = mid - divisible_by_both
            pos_1, pos_2 = mid - divisible_1, mid - divisible_2
            # print(mid, cur_res)
            
            if cur_res >= total and pos_1 >= u1 and pos_2 >= u2:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
                
            
            