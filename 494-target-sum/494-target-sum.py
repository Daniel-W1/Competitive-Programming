class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        so at each index i have a choice and i need to do one of the choice
        
        so i have 2 states idx, and cursum 
        
        at each index i make those choices and when the whole thing is over if
        my sum is target i return 1 else 0
        and just collect all those things to get the result
        
        
                                    +(1) or -(-1)
                                +(2)  (0) or   
                                
        '''
        @cache
        def check(idx, cursum):
            if idx == len(nums):
                return int(cursum == target)
        
            choice1 = check(idx+1, cursum + nums[idx])
            choice2 = check(idx+1, cursum - nums[idx])
            
            return choice1 + choice2
        
        return check(0, 0)
        