class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # find the xor of all the elements
        cur = 0
        for num in nums:
            cur ^= num
        
        # find the least significant turned on bit
        mask = cur & -cur
        answer = [0, 0]
        
        # separate the numbers
        for num in nums:
            if num & mask:
                 answer[0] ^= num
            else:
                 answer[1] ^= num
        
        return answer
                
        