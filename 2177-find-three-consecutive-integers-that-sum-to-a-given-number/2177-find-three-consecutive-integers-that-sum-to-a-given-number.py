class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        return [(num-2)//3,(num-2)//3 + 1,(num-2)//3 + 2] if sum([(num-2)//3,(num-2)//3 + 1,(num-2)//3 + 2]) == num else []