class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        leftr, leftc = 0, 0
        rightr, rightc = len(matrix)-1, len(matrix[0])-1
        seen = set()
        while leftr <= rightr or leftc <= rightc:
            midr = (leftr+rightr)//2
            midc = (leftc + rightc)//2
            if (midr, midc) in seen:
                break
            seen.add((midr, midc))
            if matrix[midr][midc] == target:
                return True
            elif matrix[midr][midc] > target:
                rightc = midc - 1
                if rightc < 0:
                    rightc = len(matrix[0])-1
                    rightr = midr - 1
            elif matrix[midr][midc] < target:
                leftc = midc + 1
                if leftc == len(matrix[0]):
                    leftc = 0
                    leftr = midr + 1
        return False
                    
        
        