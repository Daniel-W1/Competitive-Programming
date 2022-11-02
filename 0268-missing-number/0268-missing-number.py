class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # xor means exclusive or ryt
        # 011, 000, 001
        # 000, 001 , 010
        
        answer = 0
        for idx, num in enumerate(nums):
            answer ^= idx
            answer ^= num
        
        answer ^= len(nums)
        return answer
        