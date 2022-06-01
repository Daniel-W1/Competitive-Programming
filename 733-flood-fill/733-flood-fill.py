class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)-1
        n = len(image[0])-1
        check = {}
        def dfs(a,b,prev):
            if a > m or b > n or a < 0 or b < 0 or (a,b) in check:
                return 
            if image[a][b] != prev:
                return
            check[a,b] = True
            prev = image[a][b]
            image[a][b] = newColor
            dfs(a+1,b,prev)
            dfs(a-1,b,prev)
            dfs(a,b+1,prev)
            dfs(a,b-1,prev)
        dfs(sr,sc,image[sr][sc])
        return image