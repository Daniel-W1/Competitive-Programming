class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        lastday = days[-1]
        
        @cache
        def dfs(curday):
            idx = bisect_left(days, curday)
            if idx == len(days):
                return 0
            
            curday = days[idx]
            choice1 = dfs(curday + 1) + costs[0]
            choice2 = dfs(curday + 7) + costs[1]
            choice3 = dfs(curday + 30) + costs[2]
            
            return min(choice1, choice2, choice3)
        
        return dfs(1)
        
            
            
                