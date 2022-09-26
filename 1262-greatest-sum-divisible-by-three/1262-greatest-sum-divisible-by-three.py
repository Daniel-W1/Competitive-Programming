class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        '''
        1, 3, 5, 6, 8
        
        1: 1
        2: 8, 5
        0: 6, 3
        
        1,4,4, 2
        
        
        '''
        ones = []
        twos = []
        ans = 0
        for num in nums:
            if num%3 == 1:
                if len(ones) < 2:
                    heappush(ones, -num)
                else:
                    heappushpop(ones, -num)
                    
            elif num%3 == 2:
                if len(twos) < 2:
                    heappush(twos, -num)
                else:
                    heappushpop(twos, -num)
            ans += num
        
        choice1, choice2 = float('inf'), float('inf')
        # print(ones, twos, ans%3)
        if ans%3 == 1:
            if ones:
                choice1 = -max(ones)
            if len(twos) > 1:
                choice2 = -sum(twos)
                
            ans -= min(choice1, choice2)
        elif ans%3 == 2:
            if len(ones) > 1:
                choice1 = -sum(ones)
            if twos:
                choice2 = -max(twos)
            
            ans -= min(choice1, choice2)
        
        return ans if not ans%3 else 0
        
        