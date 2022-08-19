class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # first let's count the number of fresh oranges
        fresh_count = 0
        for row in grid:
            fresh_count += row.count(1)
        minutes = 0
        direc = [(1,0),(0,1),(-1, 0),(0,-1)]
        while fresh_count > 0:
            infected = set()
            for idx, row in enumerate(grid):
                for cidx, elmnt in enumerate(row):
                    if grid[idx][cidx] == 2:
                        for d in direc:
                            cr, cc = d
                            newc = cidx + cc
                            nidx = idx + cr
                            if newc >= 0 and newc < len(grid[0]) and nidx >= 0 and nidx < len(grid):
                                if grid[nidx][newc] == 1:
                                    infected.add((nidx,newc))
            # print(fresh_count, infected)
            for coordinate in infected:
                row, col = coordinate
                grid[row][col] = 2
                fresh_count -= 1
            if not infected and fresh_count > 0: return -1
            minutes += 1
        return minutes