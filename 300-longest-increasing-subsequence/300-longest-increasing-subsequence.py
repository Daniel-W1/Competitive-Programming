class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        temp = [nums[0]]
        
        '''
        [0,1,0,3,2,3]
        
        0, 1, 2, 3 
        
        [7,7,7,7,7,7]
        
        
        [10,9,2,5,3,7,101,18]
        
        2 3  
        '''
        for idx in range(1, len(nums)):
            num = nums[idx]
            insert = bisect_left(temp, num)
            
            if insert == len(temp):
                temp.append(num)
            
            elif temp[insert] > num:
                temp[insert] = num
        
        return len(temp)