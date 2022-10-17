class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort()
        
        @cache
        def dfs(idx, time):
            if idx >= n:
                return 0
            
            choice1 = dfs(idx + 1, time + 1) + (time + 1)*satisfaction[idx]
            choice2 = dfs(idx + 1, time)
            
            return max(choice1, choice2)
        
        return dfs(0, 0)