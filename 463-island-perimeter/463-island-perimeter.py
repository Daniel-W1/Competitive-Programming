class State:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, __o: object):
        return isinstance(__o, State) and self.x == __o.x and self.y == __o.y

    def __hash__(self):
        return hash(f'{self.x} {self.y}')    

class Solution:
    def islandPerimeter(self, grid):
        n, m = len(grid), len(grid[0])
        seen = set()
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))

        def in_bound(row, col):
            return 0 <= row < n and 0 <= col < m

        def dfs(row, col):
            side = count = 0
            for dr, dc in directions:
                nrow, ncol = row + dr, col + dc
                if not in_bound(nrow, ncol) or grid[nrow][ncol] == 0:
                    side += 1
                    continue
#
                new_state = State(nrow, ncol)
                if new_state not in seen:
                    seen.add(new_state)
                    count += dfs(nrow, ncol)
            return side + count

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1 and (row, col) not in seen:
                    seen.add(State(row, col))
                    return dfs(row, col)
        return 0
