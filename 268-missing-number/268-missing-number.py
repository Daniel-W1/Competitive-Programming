class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # xor means exclusive or right
        # 011, 000, 001
        # 000, 001 , 010
        
        answer = len(nums)
        for idx, num in enumerate(nums):
            answer ^= idx
            answer ^= num
        return answer
        