class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        check_map = {}
        for i,row in enumerate(matrix):
            for j,val in enumerate(matrix[i]):
                if val == 0 and (i,j) not in check_map:
                    for k in range(len(matrix[i])):
                        if matrix[i][k] != 0:
                            matrix[i][k] = 0
                            check_map[i,k] = True
                    for c,row in enumerate(matrix):
                        if row[j] != 0:
                            row[j] = 0
                            check_map[c,j] = True
        
        