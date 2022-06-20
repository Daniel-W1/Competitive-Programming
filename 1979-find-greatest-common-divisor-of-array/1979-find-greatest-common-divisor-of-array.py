class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def dijgcd(num1,num2):
            if num1 == num2:
                return num1
            if num1 >  num2:
                return dijgcd(num1-num2,num2)
            return dijgcd(num1,num2-num1)
        return dijgcd(min(nums),max(nums))