class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # find the xor of all the elements
        cur = 0
        for num in nums:
            cur ^= num
        
        # find the least significant turned on bit
        mask = cur & -cur
        
        answer = [0, 0]
        groups = [[], []]
        # separate the numbers
        for num in nums:
            if num & mask:
                groups[0].append(num)
            else:
                groups[1].append(num)
        
        
        for idx, group in enumerate(groups):
            for num in group:
                answer[idx] ^= num
        
        return answer
                
        