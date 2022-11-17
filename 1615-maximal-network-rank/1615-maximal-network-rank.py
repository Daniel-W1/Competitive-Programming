class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = defaultdict(int)
        connected = [[False for _ in range(n)] for _ in range(n)]
        
        for n1, n2 in roads:
            degree[n1] += 1
            degree[n2] += 1
            connected[n1][n2] = True
            connected[n2][n1] = True
        
        
        ans = 0
        for node in range(n):
            for secondnode in range(node + 1, n):
                # print(node, secondnode)
                if not connected[node][secondnode]:
                    ans = max(ans, degree[node] + degree[secondnode])
                else:
                    ans = max(ans, degree[node] + degree[secondnode] - 1)
        
        return ans
            
        
        
        
        