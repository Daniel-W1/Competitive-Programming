class Solution:
    def isHappy(self, n: int) -> bool:
        check = {n:True}
        while True:
            num = str(n)
            new_num = 0
            for val in num:
                new_num += (int(val)**2)
            if new_num == 1:
                return True
            if new_num in check:
                return False
            n = new_num
            check[n] = True
        
        
                
            