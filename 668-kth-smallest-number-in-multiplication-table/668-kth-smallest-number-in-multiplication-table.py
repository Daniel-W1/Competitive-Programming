class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        '''
        so here is what am going to do
        pick a number and find how many numbers it's greater 
        
        0, 8
        mid = 4, 1,1
        4 is greater than m*1 + 1 numbers 
        
        
        find the pos of the value in every row, 
        1, m 
        so what is the idea here
        
        we look at each row and do binary search to find how many of the rows elements are smaller than our target
        we collect that and add them so it's kindof a binary search using a binary search
        
        so here is what i am thinking 
        to find out how many numbers are divisible
        that are smaller than it are divisible by it,
        
        '''
        def findout(cur):
            res = 0
            for value in range(1, m+1):
                res += (min(cur, n*value)//value)
                # print(min(cur, n*value), min(cur, n*value)//value)
            return res
        
        left, right = 1, m*n
        
        while left < right:
            mid = (left + right)//2
            check = findout(mid)
            
            if check > k-1:
                right = mid 
            else:
                left = mid + 1
                
        return left
        
        