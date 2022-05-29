class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if target <= matrix[i][j]:
                    l,h = 0,len(matrix[0])-1
                    while l <= h:
                        mid = (l+h)//2
                        if matrix[i][mid] == target:
                            return True
                        elif matrix[i][mid] > target:
                            h = mid -1
                        else:
                            l = mid + 1
                    return False
                            
                
        