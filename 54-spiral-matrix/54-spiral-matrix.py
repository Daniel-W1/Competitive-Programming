class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        matr = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matr[(i+1, j+1)] = matrix[i][j]
        num = 0
        ans = []
        right, up, down, left = True, False, False, False
        i,j = 1,1
        i_max, j_max = len(matrix), len(matrix[0])
        leng= len(matr)
        while True:           
            if right:
                while j <= j_max and (i,j) in matr:
                    ans.append(matr[i,j])
                    del matr[i,j]
                    j += 1
                    num += 1
                down, right = True, False
                j -= 1 
                i += 1
                   
            elif down:
                while i <= i_max and (i,j) in matr:
                    ans.append(matr[i,j])
                    del matr[i,j]
                    i += 1
                    num += 1
                left, down = True, False
                i -= 1
                j -= 1
                

            elif left:
                while j >= 1 and (i,j) in matr:
                    ans.append(matr[i,j])
                    del matr[i,j]
                    j -= 1
                    num += 1
                up, left = True, False
                j += 1
                i -= 1
            elif up:
                while i >= 1 and (i,j) in matr:
                    ans.append(matr[i,j])
                    del matr[i,j]
                    i -= 1
                    num += 1
                right, up = True, False
                i += 1
                j += 1

            if len(ans) == leng:
                break
               
        return ans
                
            
        
        