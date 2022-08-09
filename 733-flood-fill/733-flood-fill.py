class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image)-1, len(image[0])-1
        iBound = lambda i: i >=0 and i <= m
        jBound = lambda j: j >= 0 and j <= n
        start = image[sr][sc]
        def dfs(i,j, visited):
            if not iBound(i) or not jBound(j) or (i,j) in visited or image[i][j] != start:
                return 

            image[i][j] = color
            visited.add((i,j))
            dfs(i+1, j, visited)
            dfs(i, j+1, visited)
            dfs(i-1, j, visited)
            dfs(i, j-1, visited)
        dfs(sr, sc, set())
        return image
            
            