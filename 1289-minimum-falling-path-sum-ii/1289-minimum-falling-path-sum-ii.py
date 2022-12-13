class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        cur_dp = [0]*len(grid[0])
        
        heap = []
        for idx, val in enumerate(grid[0]):
            if len(heap) < 2:
                heappush(heap, (-val, idx))
            else:
                heappushpop(heap, (-val, idx))
        
        for rowidx in range(1, len(grid)):
            for colidx in range(len(grid[0])):
                if colidx != heap[1][1]:
                    cur_dp[colidx] = grid[rowidx][colidx] - heap[1][0]
                else:
                    cur_dp[colidx] = grid[rowidx][colidx] - heap[0][0]
            
            heap = []
            for colidx, val in enumerate(cur_dp):
                if len(heap) < 2:
                    heappush(heap, (-val, colidx))
                else:
                    heappushpop(heap, (-val, colidx))
            # print(cur_dp, heap)

        res = min(cur_dp)
        return res if res else min(grid[0])
                