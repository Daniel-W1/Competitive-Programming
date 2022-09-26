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
                ones.append(num)
            elif num%3 == 2:
                twos.append(num)
            else:
                ans += num
        
        
            
#         while len(ones) >= 3:
#             for _ in range(3):
#                 ans += -heappop(ones)
#         while len(twos) >= 3:
#             for _ in range(3):
#                 ans += -heappop(twos)
                
#         while ones and twos:
#             one, two = -heappop(ones), -heappop(twos)
#             ans += one + two
        res = sum(ones) + sum(twos)
        ans += res
        
        # print(ans, ans%3)
        # print(ones, twos)
        
        choice1, choice2 = float('inf'), float('inf')
        if ans%3 == 1:
            if ones:
                choice1 = min(ones)
            if len(twos) > 1:
                choice2 = sum(sorted(twos)[:2])
            ans -= min(choice1, choice2)
        elif ans%3 == 2:
            if len(ones) > 1:
                choice1 = sum(sorted(ones)[:2])
            if twos:
                choice2 = min(twos)
            
            ans -= min(choice1, choice2)
        return ans if not (ans)%3 else 0
        
        