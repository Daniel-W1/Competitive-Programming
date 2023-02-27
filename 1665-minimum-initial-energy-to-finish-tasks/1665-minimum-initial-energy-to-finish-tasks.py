class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        
        '''
            just because it says the min it looks like BS
            
            we sort them by the difference between pair[1] and pair[0] ?
        '''
        tasks.sort(key = lambda pair: pair[0] - pair[1])
        # print(tasks)
        
        def ok(check_value):
            
            for actual, minimum in tasks:
                if check_value < minimum:
                    return False
                
                check_value -= actual
            
            return True
        
        left, right = 0, 10**20
        best = -1
        
        while left <= right:
            mid = (left + right)//2
            
            if ok(mid):
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return best