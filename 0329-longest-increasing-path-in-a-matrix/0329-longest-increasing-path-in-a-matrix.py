class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # it says longest increasing path
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        out_degrees = defaultdict(list)
        in_degrees = defaultdict(int)
        
        m, n = len(matrix), len(matrix[0])
        for r in range(m):
            for c in range(n):
                cur = matrix[r][c]
                for dx, dy in directions:
                    row, col = r + dx, c + dy
                    if 0 <= row < m and 0 <= col < n:
                        if matrix[row][col] < cur:
                            out_degrees[(r, c)].append((row, col))
                            in_degrees[(row, col)] += 1
        
        q = deque([])
        for r in range(m):
            for c in range(n):
                if (r, c) not in in_degrees:
                    q.append((r, c))
        
        # print(q)
        ans = 0
        while q:
            for _ in range(len(q)):
                curr, curc = q.popleft()
                for dx, dy in directions:
                    newx, newy = curr + dx, curc + dy
                    if 0 <= newx < m and 0 <= newy < n:
                        if matrix[newx][newy] < matrix[curr][curc]:
                            in_degrees[(newx,newy)] -= 1
                            
                            if in_degrees[(newx, newy)] == 0:
                                q.append((newx, newy))
            ans += 1
        
        return ans
                
            
        
        