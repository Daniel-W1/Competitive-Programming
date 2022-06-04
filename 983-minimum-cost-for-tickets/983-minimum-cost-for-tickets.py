from functools import lru_cache
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # hashset = set(days)
        # memo = {}
        # def findmin(day, cost):
        #     if (day,cost) not in memo:
        #         if day > days[-1]:
        #             return cost
        #         if day not in hashset:
        #             for d in range(day+1, 366):
        #                 if d in hashset:
        #                     day = d
        #                     break
        #         memo[day,cost] = min(findmin(day+1, cost+costs[0]),findmin(day+7,cost+costs[1]),findmin(day+30,cost+costs[2]))
        #     return memo[day,cost]
        # return findmin(days[0], 0)

        dayset = set(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i):
            if i > 365:
                return 0
            elif i in dayset:
                return min(dp(i + d) + c
                           for c, d in zip(costs, durations))
            else:
                return dp(i + 1)

        return dp(1)