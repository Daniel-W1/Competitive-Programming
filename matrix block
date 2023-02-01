class Solution:
    def matrixBlockSum(self, mat, K: int) -> List[List[int]]:
        m,n=len(mat),len(mat[0])
        table = [[0]*(n+1) for _ in range(m+1)]
        # res=table.copy()
        for i in range(m):
            for j in range(n):
                table[i+1][j+1]=mat[i][j]+table[i+1][j]+table[i][j+1]-table[i][j]
        for i in range(m):
            for j in range(n):
                rol1=i+K+1 if i+K+1<m+1 else m
                rol2=i-K if i-K>=0 else 0
                col1=j+K+1 if j+K+1<n+1 else n
                col2=j-K if j-K>=0 else 0
                mat[i][j]=table[rol1][col1]-table[rol1][col2]-table[rol2][col1]+table[rol2][col2]
        return mat
