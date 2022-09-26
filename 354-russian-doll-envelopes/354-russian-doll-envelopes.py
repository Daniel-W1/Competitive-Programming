class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        '''
        [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
        
        2, 3, 4, 5, 6, 7
        100, 200, 250, 300, 360, 370, 380, 400, 500
        '''
        envelopes.sort(key = lambda pair: (pair[0], -pair[1]))
        
        heights = [h for w, h in envelopes]
        def lic(nums):
            temp = [nums[0]]
            for idx in range(1, len(nums)):
                num = nums[idx]
                insert = bisect_left(temp, num)
                if insert == len(temp):
                    temp.append(num)

                elif temp[insert] > num:
                    temp[insert] = num
        
            return len(temp)
        return lic(heights)
            